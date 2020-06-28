import time


class Timer:
    def __init__(self):
        self.start_time = None
        self.job = None

    def start(self, job, verbal=False):
        self.job = job
        self.start_time = time.time()
        if verbal:
            print("[I] {job} started.".format(job=self.job))

    def stop(self):
        if self.job is None:
            return None
        elapsed_time = time.time() - self.start_time
        print("[I] {job} finished in {elapsed_time:0.3f} s."
              .format(job=self.job, elapsed_time=elapsed_time))
        self.job = None


class Log:
    verbose = True

    @staticmethod
    def log(text):
        if Log.verbose:
            print(text)
