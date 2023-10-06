import wavelink
async def node_connect(bot):
    """
    Connects the bot to a wavelink node.
    """
    # Create a wavelink Node object with the specified URI, password, and secure settings
    #node = wavelink.Node(uri=f'{config.HOST}:{config.PORT}', password=config.PASSWORD, secure=config.SECURE)
    node= wavelink.Node(uri=f'54.38.198.24:88', password="stonemusicgay", secure=False)
    node1= wavelink.Node(uri= "horizxon.studio:422",password= "horizxon.studio", secure= True)
    
    # Connect the bot to the node
    await wavelink.NodePool.connect(client=bot, nodes=[node])
    
    # Enable autoplay for wavelink player
    wavelink.Player.autoplay = False
