import re
import sys
import matplotlib.pyplot as plt
from typing import List, Tuple, Optional

def parse_log(file_path: str) -> Tuple[List[int], List[float], List[Optional[float]]]:
    steps, train_losses, val_losses = [], [], []
    
    # Упрощённые регулярные выражения
    step_pattern = re.compile(r'📊 Шаг\s+(\d+)\s+\|\s+Train Loss:\s+([\d.]+)')
    val_pattern = re.compile(r'Validation Loss:\s+([\d.]+)')  # ищем просто фразу без привязки к началу строки
    
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:  # utf-8-sig автоматически удалит BOM
            lines = f.readlines()
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return [], [], []
    
    # Диагностика: выведем первые 10 строк в сыром виде
    print("--- Первые 10 строк файла (в repr) ---")
    for i, line in enumerate(lines[:10]):
        print(f"{i}: {repr(line)}")
    print("--- Конец диагностики ---\n")
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        step_match = step_pattern.search(line)
        if step_match:
            step = int(step_match.group(1))
            train_loss = float(step_match.group(2))
            val_loss = None
            
            # Ищем Validation Loss в следующих нескольких строках (до 5 строк)
            for offset in range(1, 6):
                if i + offset >= len(lines):
                    break
                next_line = lines[i + offset].strip()
                val_match = val_pattern.search(next_line)
                if val_match:
                    val_loss = float(val_match.group(1))
                    i += offset  # пропускаем обработанные строки
                    break
            
            steps.append(step)
            train_losses.append(train_loss)
            val_losses.append(val_loss)
        
        i += 1
    
    return steps, train_losses, val_losses

def plot_losses(steps, train_losses, val_losses):
    print(f"Всего записей: {len(steps)}")
    print(f"Train Loss: {len(train_losses)} значений")
    val_count = sum(1 for v in val_losses if v is not None)
    print(f"Validation Loss: {val_count} значений")
    
    if val_count > 0:
        print("Примеры Validation Loss (шаг, значение):")
        for s, v in zip(steps, val_losses):
            if v is not None:
                print(f"  {s}: {v}")
                break
    else:
        print("Validation Loss не найден. Проверьте вывод первых строк выше.")
    
    if not steps:
        print("Нет данных.")
        return
    
    plt.figure(figsize=(12, 6))
    plt.plot(steps, train_losses, label='Train Loss', marker='o', linestyle='-', markersize=3)
    
    val_steps = [s for s, v in zip(steps, val_losses) if v is not None]
    val_values = [v for v in val_losses if v is not None]
    if val_steps:
        plt.plot(val_steps, val_values, label='Validation Loss', marker='s', linestyle='--', markersize=3)
    else:
        print("На графике Validation Loss отсутствует.")
    
    plt.xlabel('Step')
    plt.ylabel('Loss')
    plt.title('Dynamics of training')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    log_file = sys.argv[1] if len(sys.argv) > 1 else "training.md"
    print(f"Чтение файла: {log_file}")
    steps, train, val = parse_log(log_file)
    plot_losses(steps, train, val)