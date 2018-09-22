#!/usr/bin/env python
# license removed for brevity

import rospy
import os.path
import os
import filetype
from std_msgs.msg import String

def VoicePlay_Callback( voice_file ):
    # Fixme: Validation check
    if( os.path.isfile( voice_file.data ) ):
        file_type = filetype.guess( voice_file.data )
        if( file_type.extension == 'wav' ):
            os.system( 'play \"%s\"' % voice_file.data )
        else:
            print( 'Unknown file: \"%s\"' % voice_file.data )
    else:
        print( 'Unknown file: %s' % voice_file.data )

if __name__ == '__main__':
    try:
        rospy.init_node( 'voice_play_node', anonymous=True )
        rospy.Subscriber( 'VoicePlay', String, VoicePlay_Callback )
        rospy.spin()
    except rospy.ROSInterruptException:
        pass