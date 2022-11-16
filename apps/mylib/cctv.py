from qpycmd import droid
import time
import os
import sys


class CCTV(object):

    def __init__(self):
        self.path = os.path.abspath(os.path.dirname(sys.argv[0]))+'/files/'
        self.isRecording = False

    def record(self, audio=False):
        if not self.isRecording:
            self.rec_start = time.strftime("%Y%m%d_%H%I%S")
            droid.native.recorderCaptureVideo(
                self.path+'videos/tmp.mp4', recordAudio=audio)
            self.isRecording = True
            return 'videos/tmp.mp4'
        return False

    def shot(self):
        if not self.isRecording:
            fn = time.strftime("%Y%m%d_%H%I%S")+".jpg"
            droid.native.cameraCapturePicture(self.path+'pictures/%s' % fn)
            return 'pictures/'+fn
        return False

    def stop(self):
        if self.isRecording:
            ft = time.strftime("%Y%m%d_%H%I%S")
            fn = 'Recording_{0}_To_{1}.mp4'.format(self.rec_start, ft)
            droid.native.recorderStop()
            self.isRecording = False
            os.rename(self.path+'videos/tmp.mp4', self.path+'videos/'+fn)
            return 'videos/'+fn
        return False

    def startWebcam(self):
        w = droid.native.webcamStart(port=9000)
        return w.error is None

    def stopWebcam(self):
        w = droid.native.webcamStop()
        return w.error is None


if __name__ == '__main__':
    pass
