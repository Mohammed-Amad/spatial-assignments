def classFactory(iface):
    from .query_generator import SQLQueryGeneratorPlugin
    return SQLQueryGeneratorPlugin(iface)
    
