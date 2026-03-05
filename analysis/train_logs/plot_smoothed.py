import re
import sys
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Optional

def smooth(data: List[float], window_size: int = 5) -> List[float]:
    """
    Простое скользящее среднее с заданным размером окна.
    Края обрабатываются частичными окнами.
    """
    if window_size < 1:
        return data
    smoothed = []
    for i in range(len(data)):
        left = max(0, i - window_size // 2)
        right = min(len(data), i + window_size // 2 + 1)
        smoothed.append(sum(data[left:right]) / (right - left))
    return smoothed

def parse_log(file_path: str) -> Tuple[List[int], List[float], List[Optional[float]]]:
    steps, train_losses, val_losses = [], [], []
    
    step_pattern = re.compile(r'📊 Шаг\s+(\d+)\s+\|\s+Train Loss:\s+([\d.]+)')
    val_pattern = re.compile(r'Validation Loss:\s+([\d.]+)')
    
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return [], [], []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        step_match = step_pattern.search(line)
        if step_match:
            step = int(step_match.group(1))
            train_loss = float(step_match.group(2))
            val_loss = None
            
            # Ищем Validation Loss в следующих нескольких строках
            for offset in range(1, 4):
                if i + offset >= len(lines):
                    break
                next_line = lines[i + offset].strip()
                val_match = val_pattern.search(next_line)
                if val_match:
                    val_loss = float(val_match.group(1))
                    i += offset
                    break
            
            steps.append(step)
            train_losses.append(train_loss)
            val_losses.append(val_loss)
        
        i += 1
    
    return steps, train_losses, val_losses

def plot_losses(steps, train_losses, val_losses, window_size=10):
    print(f"Всего записей: {len(steps)}")
    print(f"Train Loss: {len(train_losses)} значений")
    val_count = sum(1 for v in val_losses if v is not None)
    print(f"Validation Loss: {val_count} значений")
    
    if not steps:
        print("Нет данных.")
        return
    
    # Подготовка данных для сглаживания
    train_smooth = smooth(train_losses, window_size)
    
    # Для validation loss нужно учесть пропуски: будем сглаживать только по имеющимся точкам,
    # но чтобы линия не прерывалась, создадим список с None для пропусков.
    val_values_full = [v if v is not None else np.nan for v in val_losses]
    # Сглаживаем, заменяя NaN на интерполированные? Лучше сгладить только по существующим точкам,
    # а на графике отображать с разрывами. Поэтому оставим как есть.
    
    plt.figure(figsize=(14, 7))
    
    # Исходные данные (полупрозрачные точки)
    plt.scatter(steps, train_losses, color='blue', alpha=0.3, s=10, label='Train Loss (raw)')
    if val_count > 0:
        val_steps = [s for s, v in zip(steps, val_losses) if v is not None]
        val_values = [v for v in val_losses if v is not None]
        plt.scatter(val_steps, val_values, color='orange', alpha=0.3, s=10, label='Validation Loss (raw)')
    
    # Сглаженные линии
    plt.plot(steps, train_smooth, color='blue', linewidth=2, label=f'Train Loss (smoothed, window={window_size})')
    
    if val_count > 0:
        # Для validation loss сглаживаем только по точкам, где значение есть
        # Создадим массивы без пропусков
        val_indices = [i for i, v in enumerate(val_losses) if v is not None]
        if len(val_indices) > window_size:
            val_smooth = smooth([val_losses[i] for i in val_indices], window_size)
            plt.plot([steps[i] for i in val_indices], val_smooth, color='orange', linewidth=2, label=f'Validation Loss (smoothed, window={window_size})')
        else:
            # Если слишком мало точек, просто соединим их линией
            plt.plot(val_steps, val_values, color='orange', linewidth=1, linestyle='--', label='Validation Loss (raw)')
    
    plt.xlabel('Step')
    plt.ylabel('Loss')
    plt.title('Dynamics of training')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    log_file = sys.argv[1] if len(sys.argv) > 1 else "training.md"
    # Можно передать размер окна вторым аргументом, например: python script.py training.md 15
    window = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    print(f"Чтение файла: {log_file}, окно сглаживания: {window}")
    steps, train, val = parse_log(log_file)
    plot_losses(steps, train, val, window_size=window)