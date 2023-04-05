import os 

class RunDocker:
    def __init__(self, image, extend):
        self.image = image
        self.name = 'pipeswitch-%s' % extend

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
    with RunDocker('pipeswitch:ready_model', 'test') as rd:
        # Start the server: ready_model
        rd.run('python PipeSwitch/scripts/environment/container_run_warmup.py')
        # rd.run('pwd; ls')

if __name__ == '__main__':
    main()