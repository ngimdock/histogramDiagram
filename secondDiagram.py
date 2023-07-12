from format import Format
from data import FormatName
from utils import createHistogram

firstDiagramDataset = [
  Format(FormatName.BSON.value, 223, "#F9ADA0"),
  Format(FormatName.CBOR.value, 118, "#CE5D5B"),
  Format(FormatName.FLEX_BUFFERS.value, 176, "#208CF6"),
  Format(FormatName.MASSAGE_PACK.value, 118, "#5C6468"),
  Format(FormatName.SMILES.value, 127, "#46B073"),
  Format(FormatName.UB_JSON.value, 151, "#BBB771"),
]


format_names = [format.name for format in firstDiagramDataset]
sizes = [format.size for format in firstDiagramDataset]
bar_colors = [format.barColor for format in firstDiagramDataset]


createHistogram(format_names, sizes, bar_colors)

