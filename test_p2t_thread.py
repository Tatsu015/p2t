import datetime
import unittest

from snipper import Snipper
from translator import Translator
from p2t import P2T
from p2t_thread import P2TThread
import time
import pyperclip


class TestP2TThread(unittest.TestCase):
    def setUp(self):
        print("=================================")
        print("In method", self._testMethodName)
        print("---------------------------------")

    def test_start_end(self):
        s = Snipper()
        t = Translator()
        p = P2T(s, t)
        p2t = P2TThread(p)

        p2t.exec()
        p2t.exit()

        self.assertEqual(True, True)

    def test_start_pause_end(self):
        s = Snipper()
        t = Translator()
        p = P2T(s, t)
        p2t = P2TThread(p)

        p2t.exec()
        p2t.pause()
        p2t.exit()

        self.assertEqual(True, True)

    def test_start_pause_start_end(self):
        s = Snipper()
        t = Translator()
        p = P2T(s, t)
        p2t = P2TThread(p)

        p2t.exec()
        p2t.pause()
        p2t.exec()
        p2t.exit()

        self.assertEqual(True, True)

    def test_start_pause_start_pause_end(self):
        s = Snipper()
        t = Translator()
        p = P2T(s, t)
        p2t = P2TThread(p)

        p2t.exec()
        p2t.pause()
        p2t.exec()
        p2t.pause()
        p2t.exit()

        self.assertEqual(True, True)

    # capture
    def test_start_capture_capture_end(self):
        s = Snipper()
        t = Translator()
        p = P2T(s, t)
        p2t = P2TThread(p)

        p2t.exec()
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)
        p2t.exit()

        self.assertEqual(True, True)

    def test_start_capture_capture_pause_end(self):
        s = Snipper()
        t = Translator()
        p = P2T(s, t)
        p2t = P2TThread(p)

        p2t.exec()
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)
        p2t.pause()
        p2t.exit()
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)

        self.assertEqual(True, True)

    def test_start_capture_capture_pause_start_capture_capture_end(self):
        s = Snipper()
        t = Translator()
        p = P2T(s, t)
        p2t = P2TThread(p)

        p2t.exec()
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)
        p2t.pause()
        p2t.exec()
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)
        p2t.exit()

        self.assertEqual(True, True)

    def test_start_capture_capture_pause_start_capture_capture_pause_end(self):
        s = Snipper()
        t = Translator()
        p = P2T(s, t)
        p2t = P2TThread(p)

        p2t.exec()
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)
        p2t.pause()
        p2t.exec()
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)
        pyperclip.copy(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}")
        time.sleep(1)
        p2t.pause()
        p2t.exit()

        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
