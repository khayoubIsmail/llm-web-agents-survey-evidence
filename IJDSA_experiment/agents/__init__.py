from .direct_dom import DirectDOMSnapshotAgent
from .ground_verify import SchemaStateGroundVerifyAgent
from .playwright_mcp import PlaywrightMCPReActAgent

REGISTRY = {
    'A1': DirectDOMSnapshotAgent,
    'A2': SchemaStateGroundVerifyAgent,
    'A3': PlaywrightMCPReActAgent,
}
