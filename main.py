# main.py

from pylatex import Document, Section, Command, NoEscape, Package, Figure, NewLine, Subsection
from pylatex.utils import bold
import parts.configuration as config
from utils.build import generate_pdf
from parts.cover import add_cover
from parts.about import add_about
from parts.requirements import add_requirements
from parts.timetable import add_timetable
from parts.conclusion import add_conclusion
from parts.description import add_description
from parts.generativeAI import makeQuestion

doc = Document('article')
doc.packages.append(Package('geometry'))
doc.packages.append(Package('setspace'))
doc.packages.append(Package('booktabs'))
doc.packages.append(Package('float'))
doc.packages.append(Package('graphicx'))
doc.packages.append(Package('pgfgantt'))



doc.preamble.append(NoEscape(r'\renewcommand{\contentsname}{Summary}'))

# Adiciona logo ao preâmbulo
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))

# Chama a função que adiciona a capa
add_cover(doc)

doc.append(NoEscape(r'\newgeometry{top=3.5cm, bottom=2cm, left=2cm, right=2cm}'))


# Personalizar o cabeçalho com imagens e texto centralizado
# Definição do cabeçalho com imagem e texto
doc.preamble.append(Command('usepackage', 'fancyhdr'))
doc.preamble.append(NoEscape(r'\pagestyle{fancy}'))
doc.preamble.append(NoEscape(r'\setlength{\headwidth}{510pt}'))
doc.preamble.append(NoEscape(r'\fancyhead[L]{\includegraphics[width=2cm]{frigel-logo.png}}'))  # canto esquerdo
doc.preamble.append(NoEscape(r'\fancyhead[C]{\textbf{Project Proposal}}'))         # centro
doc.preamble.append(NoEscape(r'\fancyhead[R]{\includegraphics[width=1cm]{unifi-logo.png}}'))  # canto direito
doc.append(NoEscape(r'\onehalfspacing'))
doc.append(NoEscape(r'\setlength{\parindent}{12pt}'))

doc.preamble.append(NoEscape(r'\setlength{\headheight}{2cm}'))

doc.append(Command('tableofcontents'))
doc.append(Command('newpage'))

add_about(doc)
doc.append(Command('newpage'))
add_description(doc)

doc.append(Command('newpage'))
add_timetable(doc)

doc.append(Command('newpage'))
add_conclusion(doc)

# Gera o PDF
generate_pdf(doc, 'Results/documento_com_capa', clean_tex=False)
