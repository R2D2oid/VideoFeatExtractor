import cv2

def get_frame_snapshot_at(input_vid, sec):
    '''
    obtains a snapshot frame of the video at the given second
    
    Args:
        input_vid: cv2.VideoCapture of the input video
        sec: int 

    Returns:
        hasFrames: Boolean
        image: array2d 
    '''
    input_vid.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    hasFrames, image = input_vid.read()
    if hasFrames:
        return hasFrames, image
    return False, None

def get_video_frames(input_vid, output_dir, start_sec = 0, end_sec = 10000, fps = 10):
    '''
    splits a given input video break it into image frames and stores them in the output dir
    
    Args:
        input_vid: cv2.VideoCapture of the input video
        output_dir: string directory path where the output frames will be stored
        fps: int frame per second

    Returns:
        None
    '''
    frameRate = 1.0/fps
    
    sec = start_sec
    count = 0
    hasFrames = True

    # make sure the output_dir format is properly set
    if output_dir[-1] != '/':
        output_dir = '{}/'.format(output_dir)

    while hasFrames:
        if sec > end_sec:
            break
        hasFrames, image = get_frame_snapshot_at(input_vid, sec)
        count += 1
        sec += frameRate
        sec = round(sec, 2)

        if hasFrames: cv2.imwrite(output_dir + '{:06d}.jpg'.format(count), image) 
    return count-1
