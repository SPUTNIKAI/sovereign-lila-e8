# Training Scripts

## Available Scripts

### Start Training (tmux)
```bash
./scripts/start_training.sh
```
Starts training in detached tmux session `lila-train`

### Run Training (direct)
```bash
./scripts/run_training.sh
```
Runs training directly in current terminal

### Monitor Training
```bash
./scripts/monitor_training.sh
```
Shows training status and recent output

### Check Training
```bash
./scripts/check_training.sh
```
Quick status check of training log

## Usage

```bash
# Start in background
./scripts/start_training.sh

# Monitor
./scripts/monitor_training.sh

# Attach to session
tmux attach -t lila-train

# Detach: Ctrl+b d

# Stop
tmux kill-session -t lila-train
```
