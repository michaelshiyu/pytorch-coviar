import argparse

import numpy as np
import skimage.io as io

from coviar import load

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("--load_dir", type=str)
  parser.add_argument("--gop_idx", type=int, default=0)
  parser.add_argument("--frame_idx", type=int, default=0)
  parser.add_argument("--repr", type=int, default=0)
  parser.add_argument("--accumulate", type=bool, default=True)
  parser.add_argument("--save_dir", type=str, default="./frame.png")

  args = parser.parse_args()
  
  frame = load(args.load_dir, args.gop_idx, args.frame_idx, args.repr, args.accumulate)
  print(np.max(frame), frame[frame<0], frame.dtype, frame.shape)
  # io.imsave(args.save_dir, frame)
