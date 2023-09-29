import os
import sys
import argparse
py = sys.executable
os.chdir(os.path.dirname(os.path.abspath(__file__)))


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataset", default=f'{os.getcwd()}/../hulc-data/task_D_D')
args = parser.parse_args()

# execute tmux
os.system(f'''tmux new-session -d -s calvin_cache_dataset''')
os.system(f'''tmux send-keys -t calvin_cache_dataset 'cd {os.getcwd()}' Enter''')
os.system(f'''tmux send-keys -t calvin_cache_dataset '{py} hulc/training.py datamodule.root_data_dir={args.dataset} model=dummy logger=tb_logger trainer.gpus=1' Enter''')
print('View dataset caching progress with: \ntmux a -t calvin_cache_dataset')