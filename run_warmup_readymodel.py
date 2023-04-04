import os 

class RunDocker:
    def __init__(self, image):
        self.image = image
        self.name = 'pipeswitch'

    def __enter__(self):
        os.system('docker run --name %s --rm -it -d --gpus all -w /workspace %s bash' % (self.name, self.image))
        self.run('git clone https://github.com/tuanmanh1410/PipeSwitch.git')
        return self

    def __exit__(self, *args, **kwargs):
        os.system('docker stop %s' % self.name)

    def run(self, cmd):
        print("Run command:")
        os.system('docker exec -w /workspace %s %s' % (self.name, cmd))


def main():
    with RunDocker('pipeswitch:ready_model') as rd:
        # Start the server: ready_model
        rd.run('python PipeSwitch/scripts/environment/container_run_warmup.py')

if __name__ == '__main__':
    main()