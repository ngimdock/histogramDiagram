from format import Format
from data import FormatName
from utils import createHistogram

firstDiagramDataset = [
  Format(FormatName.BSON.value, 223, "#BBB771"),
  Format(FormatName.CBOR.value, 118, "#CE5D5B"),
  Format(FormatName.FLEX_BUFFERS.value, 176, "#F4A361"),
  Format(FormatName.MASSAGE_PACK.value, 118, "#208CF6"),
  Format(FormatName.SMILES.value, 127, "#208CF6"),
  Format(FormatName.UB_JSON.value, 151, "#208CF6"),
]

# Create lists of format names, sizes, and bar colors
format_names = [format.name for format in firstDiagramDataset]
sizes = [format.size for format in firstDiagramDataset]
bar_colors = [format.barColor for format in firstDiagramDataset]


createHistogram(format_names, sizes, bar_colors)

