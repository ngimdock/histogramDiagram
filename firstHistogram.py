from format import Format
from data import FormatName
from utils import createHistogram

firstDiagramDataset = [
  Format(FormatName.ASN_1.value, 44, "#BBB771"),
  Format(FormatName.APACHE_AVRO.value, 56, "#5B3758"),
  Format(FormatName.MICROSOFT_BOND.value, 77, "#F4A361"),
  Format(FormatName.CAPTN_PROTO.value, 83, "#208CF6"),
  Format(FormatName.FLAT_BUFFERS.value, 208, "#46B073"),
  Format(FormatName.PROCOLE_BUFFERS.value, 64, "#CE5D5B"),
  Format(FormatName.APACHE_THRIFT.value, 64, "#5C6468"),
]


format_names = [format.name for format in firstDiagramDataset]
sizes = [format.size for format in firstDiagramDataset]
bar_colors = [format.barColor for format in firstDiagramDataset]

createHistogram(format_names, sizes, bar_colors)

