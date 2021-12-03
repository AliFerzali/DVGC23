from canlib import canlib, Frame

def read(channel, func = None, frame = None, params = []):
    """Reads Frames from a channel and optionally runs them through a function, returns the Frame.
 
    :param channel: the channel from whtch the frames are read
    :type channel: canlib.Channel
    :param func: the functions to run the Frames through, defaults to None
    :type func: callable, optional
    :param frame: if provided, this frame will be used instead of reading from channel, defaults to None
    :type frame: canlib.Frame, optional
    :param params: list of parametes to pass to func, defaults to []
    :type params: list, optional
    :raises TypeError: if parameters are of the wrong type
    
    :rtype: canlib.Frame, None
    :return: frame, None
    """
    if(frame is not None and not isinstance(frame, Frame)):
        raise TypeError("The passed frame is not a canlib Frame!")
    if(not isinstance(channel, canlib.channel.Channel)):
        raise TypeError("The channel is not a proper canlib Channel!")
    while True:
        try:
            if(frame is None):
                frame = channel.read()
            if(func is None):
                return frame
            return func(frame, params)
        except (canlib.canNoMsg) as ex:
            return None
    

            
