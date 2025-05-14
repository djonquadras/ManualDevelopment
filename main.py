# main.py

from pylatex import Document, Command, NoEscape, Package
from utils.build import generate_pdf
from parts.cover import add_cover
from parts.about import add_about
from parts.timetable import add_timetable
from parts.conclusion import add_conclusion
from parts.description import add_description

# Create the document
doc = Document('article')

# Import all the required packages
doc.packages.append(Package('geometry'))
doc.packages.append(Package('setspace'))
doc.packages.append(Package('booktabs'))
doc.packages.append(Package('float'))
doc.packages.append(Package('graphicx'))
doc.packages.append(Package('pgfgantt'))


# Change the summary name
doc.preamble.append(NoEscape(r'\renewcommand{\contentsname}{Summary}'))

# Add the cover
add_cover(doc)

# Change the page layout
doc.append(NoEscape(r'\newgeometry{top=3.5cm, bottom=2cm, left=2cm, right=2cm}'))

# Change header
doc.preamble.append(Command('usepackage', 'fancyhdr'))
doc.preamble.append(NoEscape(r'\pagestyle{fancy}'))
doc.preamble.append(NoEscape(r'\setlength{\headwidth}{510pt}'))
doc.preamble.append(NoEscape(r'\fancyhead[L]{\includegraphics[width=2cm]{frigel-logo.png}}'))  # canto esquerdo
doc.preamble.append(NoEscape(r'\fancyhead[C]{\textbf{Project Proposal}}'))         # centro
doc.preamble.append(NoEscape(r'\fancyhead[R]{\includegraphics[width=1cm]{unifi-logo.png}}'))  # canto direito
doc.append(NoEscape(r'\onehalfspacing'))
doc.append(NoEscape(r'\setlength{\parindent}{12pt}'))
doc.preamble.append(NoEscape(r'\setlength{\headheight}{2cm}'))

# Create the summary
doc.append(Command('tableofcontents'))
doc.append(Command('newpage'))

# Add the "About" Section
add_about(doc)
doc.append(Command('newpage'))

# Add the "Proposed Model" section
add_description(doc)
doc.append(Command('newpage'))

# Add the timetable and activities section
add_timetable(doc)

# Add the final section
doc.append(Command('newpage'))
add_conclusion(doc)

# Generate PDF
generate_pdf(doc, 'Results/documento_com_capa', clean_tex=False)
