# tweener-rez

Tweener is a tool similar to TweenMachine or aTools/animBot. It allows you to quickly create inbetweens or 
adjust existing keys by interpolating towards adjacent keyframes, and can 
speed-up your workflow when creating breakdowns and inbetweens.

## Run the tool
    import maya.cmds as cmds
    
    if cmds.pluginInfo('tweener.py', q=True, registered=True):
        if cmds.pluginInfo('tweener.py', q=True, loaded=False):
            cmds.loadPlugin('tweener.py')
        cmds.tweener()
    else:
        cmds.warning('tweener.py is not registered')