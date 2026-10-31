# mission_2

## choice
I recommend the learned YOLOX detector with a low acceptance threshold of 0.05. On normal, dim, and occluded images, it found all 6 mugs with 0 false boxes, while the classical rule failed on both dim images. Across all images at 0.05, the learned detector had 16 correct, 2 false, and 4 missed boxes. It had the same box recall with fewer wrong-object boxes. The cost is time: about 32-36 ms per image versus about 3 ms for the classical rule. That is still fast for a desk-assistance robot that does not need to react in milliseconds. A threshold this low should be watched for false boxes in more cluttered scenes.

On normal_1, the class-agnostic U2-Net foreground mask at threshold 0.50 has mask IoU 0.576 and Dice 0.731 against the visible-mug mask, with 4,453 extra pixels and 1,852 missed mug pixels. The mask has no class label: it marks whatever is visually noticeable, so the extra pixels come from other desk items and background, and a high IoU just means the regions overlap. It cannot tell the robot which foreground blob is the mug versus the laptop or keyboard, so it would need a detector or classifier to supply the identity, plus depth and calibration before any grasp.

Important limit: this is a very small test (31 images, only 2 mug images per condition, one mug and one desk scene with mostly synthetic changes like dimming and occlusion). A single image changes a condition's score by 50%, and the result may not generalize to other mugs, desks, real lighting, or real camera viewpoints.

## comparison
Saved comparison: classical = my locked Part A rule, learned = YOLOX cup detector at acceptance threshold 0.05 (3 images per condition, 2 with a mug and 1 absent).

normal: classical 2 correct, 0 false, 0 missed; learned 2 correct, 0 false, 0 missed.
dim: classical 0 correct, 2 false, 2 missed; learned 2 correct, 0 false, 0 missed.
occluded: classical 2 correct, 0 false, 0 missed; learned 2 correct, 0 false, 0 missed.

Normal and occluded are identical for the two detectors at this threshold, so they do not separate them. Both of them found every mug and put no bounding box on the image without the mug. The difference between the two is when the mug is dim. Example dim_1: the classical box is not on the mug. Dimming pushes the wood desk under my value ceiling of 110, so the desk passes the color rule and merges with the mug into one huge contour, and the largest-area rule boxes almost the whole desk. That image counts as both a false box and a missed mug. The learned detector's box on dim_1 overlaps the reference mug box (IoU >= 0.50) because it uses learned shape and appearance features rather than a fixed brightness band.

The threshold matters a lot for the learned model; using the default value 0.50, it only found 1 of 2 normal mugs and 0 of 2 dim and 0 of 2 occluded mugs. At 0.20, it got normal and dim right but missed both occluded mugs. Only at 0.05 did it match or beat the classical rule on all three conditions.
