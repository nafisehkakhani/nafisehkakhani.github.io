 # I am a research scientist at Google working on 3D computer vision and generative modeling.
 # Prior to joining Google, I was a PhD student at the <a href="https://uni-tuebingen.de/en/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/autonomous-vision/home/" target="_blank">Max Planck Insitute for Intelligent Systems</a> supervised by <a href="https://www.cvlibs.net/" target="_blank">Andreas Geiger</a>.
 # As an undergraduate student, I studied Mathematics at the <a href="http://www.mi.uni-koeln.de/main/index.en.php" target="_blank">University of Cologne (Germany)</a> and computer science as the Master's at the 
 # <a href="https://www.st-andrews.ac.uk/computer-science/" target="_blank">University of St Andrews (UK)</a>.

# In 2011, I graduated as top of my year from secondary school and received <a href="https://www.e-fellows.net/" target="_blank">the e-fellows scholarship</a> and was admitted to <a href="https://www.mathematik.de/" target="_blank">the Germany Mathematics Society</a> and <a href="https://www.dpg-physik.de/" target="_blank">the German Physics Society</a>. In 2017 I received the Dean's List Award for Academic Excellence for my Master's degree.
# During my PhD studies, I was a scholar of <a href="https://imprs.is.mpg.de/" target="_blank">the International Max Planck Research School for Intelligent Systems (IMPRS-IS)</a>.
# Our research projects Occupancy Networks, DVR, and ConvOnet were selected to be among the 15 most influencial <a href="https://www.paperdigest.org/2021/03/most-influential-cvpr-papers-2021-03/" target="_blank">CVPR</a> /  <a href="https://www.paperdigest.org/2023/09/most-influential-eccv-papers-2023-09/" target="_blank">ECCV</a> papers of 2019 and 2020.
# In 2021, we received the CS teaching award for our <a href="https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/informatik/lehrstuehle/autonomous-vision/lectures/computer-vision/" target="_blank">computer vision lecture</a> as well as  <a href="https://cyber-valley.de/en/news/meet-the-ai-gamedev-winners" target="blank">the AIGameDev scientific award</a> for our GRAF project and <a href="https://cvpr2021.thecvf.com/node/329" target="_blank">the CVPR Best Paper Award</a> for GIRAFFE (<a href="https://cyber-valley.de/en/news/best-paper-cvpr-2021" target="_blank">news coverage</a>).

# <a href="https://m-niemeyer.github.io/assets/other/bio.txt" target="_blank" style="margin-right: 5px"><i class="fa-solid fa-graduation-cap"></i> Bio</a>
# <a href="https://m-niemeyer.github.io/assets/pdf/CV_Niemeyer_Michael.pdf" target="_blank" style="margin-right: 5px"><i class="fa fa-address-card fa-lg"></i> CV</a>

from pybtex.database.input import bibtex

def get_personal_data():
    name = ["Nafiseh", "Kakhani"]
    email = "nafiseh.kakhani@thelandbankinggroup.com"
    twitter = "NafisehKakhani"
    github = "nafisehkakhani"
    linkedin = "nafiseh-kakhani"
    bio_text = f"""
                <p>
                
                I am a Remote Sensing Engineer, currently an Earth Observation and Machine Learning Scientist at
                <a href="https://www.thelandbankinggroup.com/">The Landbanking Group GmbH</a> in Munich,
                with a focus on developing the STOA model for remote sensing image processing in support of nature conservation and regenerative agriculture.

                Before that, I was a Postdoctoral Researcher at the
                University of Tuebingen (Germany) in the Geoscience Department under Prof. Dr. Thomas Scholten,
                where I applied computer vision, machine learning, and deep learning techniques to Earth observation data to extract environmental insights, particularly related to soil.

                My academic background includes a Bachelor's in Geomatics Engineering, followed by a Master's and PhD in Remote Sensing.

                </p>
                <p> Would like to connect? Feel free to contact me via mail!</p>
                <p>
                    
                    <a href="mailto:nafiseh.kakhani@uni-tuebingen.de" style="margin-right: 5px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://scholar.google.com/citations?user=b7EX1rUAAAAJ&hl=en" target="_blank" style="margin-right: 5px"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://github.com/nafisehkakhani" target="_blank" style="margin-right: 5px"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/nafiseh-kakhani-b43a6a47/" target="_blank" style="margin-right: 5px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                </p>
 """
    footer = """
            <div class="col-sm-12" style="">
                <p>
                    Website template provided by <a href="https://github.com/m-niemeyer/m-niemeyer.github.io" target="_blank">Michael Niemeyer</a>. <br>
                    <a href="https://m-niemeyer.github.io/" target="_blank">&#9883;</a>
                    <a href="https://kashyap7x.github.io/" target="_blank">&#9883;</a>
                    <a href="https://kait0.github.io/" target="_blank">&#9883;</a>
                </p>
            </div>
    """
    return name, bio_text, footer


# def get_author_dict():
#     return {
#         'Andreas Geiger': 'https://www.cvlibs.net/',
#         'Songyou Peng': 'https://pengsongyou.github.io/',
#         'Zehao Yu': 'https://niujinshuchong.github.io/',
#         'Torsten Sattler': 'https://tsattler.github.io/',
#         'Katja Schwarz': 'https://katjaschwarz.github.io/',
#         'Axel Sauer': 'https://axelsauer.com/',
#         'Jonathan Barron': 'https://jonbarron.info/',
#         'Ben Mildenhall': 'https://bmild.github.io/',
#         'Mehdi Sajjadi': 'https://msajjadi.com/',
#         'Noha Radwan': 'http://www2.informatik.uni-freiburg.de/~radwann/',
#         'Chiyu Jiang': 'https://www.maxjiang.ml/',
#         'Yiyi Liao': 'https://yiyiliao.github.io/',
#         'Marc Pollefeys': 'https://people.inf.ethz.ch/pomarc/',
#         'Michael Oechsle': 'https://moechsle.github.io/',
#         'Christian Reiser': 'https://creiser.github.io/',
#         'Lars Mescheder': 'https://scholar.google.de/citations?user=h2k1gL4AAAAJ&hl=de',
#         'Thilo Strauss': 'https://scholar.google.com/citations?user=VlymtLQAAAAJ&hl=en',
#         'Sebastian Nowozin': 'http://www.nowozin.net/sebastian/',
#         'Marie-Julie Rakotosaona': 'http://www.lix.polytechnique.fr/Labo/Marie-Julie.RAKOTOSAONA/',
#         'Fabian Manhardt': 'https://campar.in.tum.de/Main/FabianManhardt',
#         'Diego Martin Arroyo': 'https://martinarroyo.net/',
#         'Abhijit Kundu': 'https://abhijitkundu.info/',
#         'Federico Tombari': 'https://www.cs.cit.tum.de/camp/members/senior-research-scientists/federico-tombari/',
#         'Anpei Chen': 'https://apchenstu.github.io/',
#         'Bozidar Antic': 'https://bozidarantic.com/',
#         'Apratim Bhattacharyya': 'https://apratimbhattacharyya18.github.io/',
#         'Siyu Tang': 'https://inf.ethz.ch/people/person-detail.MjYyNzgw.TGlzdC8zMDQsLTg3NDc3NjI0MQ==.html',
#         'Hidenobu Matsuki': 'https://dblp.org/pid/225/4487.html',
#         'Keisuke Tateno': 'https://campar.in.tum.de/Main/KeisukeTateno',
#         'Alessio Tonioni': 'https://alessiotonioni.github.io/',
#         'Christina Tsalicoglou': 'https://scholar.google.ch/citations?user=7D10QQkAAAAJ&hl=en', 
#         'Amit Raj': 'https://amitraj93.github.io/',
#         'Srinivas Kaza': 'https://www.linkedin.com/in/srinivas-kaza-64223b74',
#         'Ben Poole': 'https://poolio.github.io/',
#         'Nataniel Ruiz': 'https://natanielruiz.github.io/',
#         'Shiran Zada': 'https://scholar.google.com/citations?user=I2qheksAAAAJ',
#         'Kfir Aberman': 'https://kfiraberman.github.io/',
#         'Michael Rubinstein': 'http://people.csail.mit.edu/mrub/',
#         'Yuanzhen Li': 'http://people.csail.mit.edu/yzli/',
#         'Varun Jampani': 'https://varunjampani.github.io/',
#         'Francis Engelmann': 'https://francisengelmann.github.io/',
#         'Mohamad Shahbazi': 'https://mohamad-shahbazi.github.io/',
#         'Liesbeth Claessens': 'https://asl.ethz.ch/the-lab/people/person-detail.MjY5NDUz.TGlzdC8xNTg0LDEyMDExMzk5Mjg=.html',
#         'Edo Collins': 'https://www.linkedin.com/in/edo-collins/?originalSubdomain=ch',
#         'Luc Van Gool': 'https://ee.ethz.ch/the-department/faculty/professors/person-detail.OTAyMzM=.TGlzdC80MTEsMTA1ODA0MjU5.html',
#         'Fangjinhua Wang': 'https://fangjinhuawang.github.io/',
#         'Richard Szeliski': 'https://szeliski.org/',
#         'Kunyi Li': 'https://campus.tum.de/tumonline/ee/ui/ca2/app/desktop/#/pl/ui/$ctx/visitenkarte.show_vcard?$ctx=design=ca2;header=max;lang=de&pPersonenGruppe=3&pPersonenId=6EC78DAA25310FF2',
#         'Nassir Navab': 'https://www.professoren.tum.de/en/navab-nassir',
#         }
# 
# 
def get_author_dict():
    return {
        'Michael Mommert': 'https://mommermi.github.io/',
        'Nikolaos Tziolas': 'https://swfrec.ifas.ufl.edu/faculty/tziolas/',
        'Thomas Scholten': 'https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/geowissenschaften/arbeitsgruppen/geographie/forschungsbereich/bodenkunde-und-geomorphologie/work-group/people-main-pages/team-profs-senior/prof-dr-thomas-scholten/',
        'Seyed-Kazem Alavipanah': 'https://alavipanah.ir/',
        'Sara Attarchi': 'https://profile.ut.ac.ir/en/~satarchi',
        'Mohammad Javad Valadan Zoej' : 'https://wp.kntu.ac.ir/valadanzouj/'
        }

# 'Mehdi Mokhtarzade',
# 'Muhammad Javad Valadan Zoej',
# 'Meisam Amani',
# 'Setareh Alamdar',
# 'Ndiyeh Kebonyeh',
# 'Ruhollah Taghizadeh',
# 'Kamal Nabiollahi',
# 'Moien Rangzan',
# 'Sara Attarchi',
# 'Seyed Kazem Alavipanah'

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Nafiseh Kakhani', add_links=True):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('last'): 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    if 'award' in entry.fields.keys():
        s += f"""<a href="{entry.fields['doi']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<a href="{entry.fields['doi']}" target="_blank">{entry.fields['title']}</a> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['journal']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'html': 'Project Page', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    for entr in ['title', 'journal', 'year']:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    # s += " /" + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

# def get_talk_entry(entry_key, entry):
#     s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
#     s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
#     s += """</div><div class="col-sm-9">"""
#     s += f"""{entry.fields['title']}<br>"""
#     s += f"""<span style="font-style: italic;">{entry.fields['journal']}</span>, {entry.fields['year']} <br>"""

#     artefacts = {'slides': 'Slides', 'video': 'Recording'}
#     i = 0
#     for (k, v) in artefacts.items():
#         if k in entry.fields.keys():
#             if i > 0:
#                 s += ' / '
#             s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
#             i += 1
#         else:
#             print(f'[{entry_key}] Warning: Field {k} missing!')
#     s += """ </div> </div> </div>"""
#     return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

# @article{kakhani2023soilnet,
#   title={SoilNet: An Attention-based Spatio-temporal Deep Learning Framework for Soil Organic Carbon Prediction with Digital Soil Mapping in Europe},
#   author={Nafiseh Kakhani and Rangzan, Moien and Jamali, Ali and Attarchi, Sara and Alavipanah, Seyed Kazem and Scholten, Thomas},
#   journal={arXiv preprint},
#   year={2023},
#   doi = {https://arxiv.org/abs/2308.03586},
#   publisher={ARXIV},
#   code = {https://github.com/moienr/SoilNet/tree/preprint_version},
#   img = {assets/img/publications/SoilNet1.png}
# }

# def get_talks_html():
#     parser = bibtex.Parser()
#     bib_data = parser.parse_file('talk_list.bib')
#     keys = bib_data.entries.keys()
#     s = ""
#     for k in keys:
#         s+= get_talk_entry(k, bib_data.entries[k])
#     return s

# def get_index_html():
#     # pub = get_publications_html()
#     # talks = get_talks_html()
#     name, bio_text, footer = get_personal_data()
#     s = f"""
#     <!doctype html>
# <html lang="en">

# <head>
#   <!-- Required meta tags -->
#   <meta charset="utf-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

#   <!-- Bootstrap CSS -->
#   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
#     integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

#   <title>{name[0] + ' ' + name[1]}</title>
#   <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
# </head>

# <body>
#     <div class="container">
#         <div class="row">
#             <div class="col-md-1"></div>
#             <div class="col-md-10">
#                 <div class="row" style="margin-top: 3em;">
#                     <div class="col-sm-12" style="margin-bottom: 1em;">
#                     <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
#                     </div>
#                     <br>
#                     <div class="col-md-10" style="">
#                         {bio_text}
#                     </div>
#                     <div class="col-md-2" style="">
#                         <img src="assets/img/linked1.JPG" class="img-thumbnail" width="280px" alt="Profile picture">
#                     </div>
#                 </div>
#                 <div class="row" style="margin-top: 1em;">
#                     <div class="col-sm-12" style="">
#                         <h4>Publications</h4>
#                         {pub}
#                     </div>
#                 </div>
#                 <div class="row" style="margin-top: 3em;">
#                     <div class="col-sm-12" style="">
#                         <h4>Talks</h4>
#                         {talks}
#                     </div>
#                 </div>
#                 <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
#                     {footer}
#                 </div>
#             </div>
#             <div class="col-md-1"></div>
#         </div?
#     </div>

#     <!-- Optional JavaScript -->
#     <!-- jQuery first, then Popper.js, then Bootstrap JS -->
#     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
#       integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
#       crossorigin="anonymous"></script>
#     <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
#       integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
#       crossorigin="anonymous"></script>
#     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
#       integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
#       crossorigin="anonymous"></script>
# </body>

# </html>
#     """
#     return s



# def get_index_html():
#     # pub = get_publications_html()
#     name, bio_text, footer = get_personal_data()
#     s = f"""
#     <!doctype html>
# <html lang="en">

# <head>
#   <!-- Required meta tags -->
#   <meta charset="utf-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

#   <!-- Bootstrap CSS -->
#   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
#     integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

#   <title>{name[0] + ' ' + name[1]}</title>
#   <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
# </head>

# <body>
#     <div class="container">
#         <div class="row">
#             <div class="col-md-1"></div>
#             <div class="col-md-10">
#                 <div class="row" style="margin-top: 3em;">
#                     <div class="col-sm-12" style="margin-bottom: 1em;">
#                     <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
#                     </div>
#                     <div class="col-md-10">
#                         {bio_text}
#                     </div>
#                 <div class="row" style="margin-top: 1em;">
#                     <div class="col-sm-12" style="">
#                         <h4>Publications</h4>
#                         {bio_text}
#                      </div>
#                     <div class="col-md-2">
#                         <img src="assets/img/linked1.JPG" class="img-thumbnail" width="280px" alt="Profile picture">
#                     </div>
#                 </div>
#                 <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
#                     {footer}
#                 </div>
#             </div>
#             <div class="col-md-1"></div>
#         </div>
#     </div>

#     <!-- Optional JavaScript; choose one of the two! -->

#     <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
#     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
#       integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
#       crossorigin="anonymous"></script>
#     <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
#       integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
#       crossorigin="anonymous"></script>
#     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
#       integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
#       crossorigin="anonymous"></script>
# </body>

# </html>
#     """
#     return s


def get_index_html():
    pub = get_publications_html()
    #talks = get_talks_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <!-- Custom CSS -->
  <link rel="stylesheet" href="assets/css/style.css">  

  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-10">
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="margin-bottom: 1em;">
                    <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
                    </div>
                    <br>
                    <div class="col-md-10" style="">
                        {bio_text}
                    </div>
                    <div class="col-md-2" style="">
                        <img src="assets/img/profile1.png" class="img-thumbnail" width="480px" alt="Profile picture">
                    </div>
        </div>
        <div class="row" style="margin-top: 2em;">
            <div class="col-sm-12" style="">
                <h4>Publications</h4>
                {pub}
            </div>
        </div>


        
        <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
            {footer}
        </div>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')