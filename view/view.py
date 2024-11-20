from flask import Blueprint, render_template, current_app
import os
import re



view_bp = Blueprint('view_bp', __name__,
                        template_folder='templates',
                        static_folder='static', static_url_path='assets')



title_to_filename = {"A Midsummer Night's Dream": 'a-midsummer-nights-dream_TXT_FolgerShakespeare.txt', "All's Well That Ends Well": 'alls-well-that-ends-well_TXT_FolgerShakespeare.txt', 'Antony and Cleopatra': 'antony-and-cleopatra_TXT_FolgerShakespeare.txt', 'As You Like It': 'as-you-like-it_TXT_FolgerShakespeare.txt', 'Coriolanus': 'coriolanus_TXT_FolgerShakespeare.txt', 'Cymbeline': 'cymbeline_TXT_FolgerShakespeare.txt', 'Hamlet': 'hamlet_TXT_FolgerShakespeare.txt', 'Henry IV, Part I': 'henry-iv-part-1_TXT_FolgerShakespeare.txt', 'Henry IV, Part 2': 'henry-iv-part-2_TXT_FolgerShakespeare.txt', 'Henry VI, Part 1': 'henry-vi-part-1_TXT_FolgerShakespeare.txt', 'Henry VI, Part 2': 'henry-vi-part-2_TXT_FolgerShakespeare.txt', 'Henry VI, Part 3': 'henry-vi-part-3_TXT_FolgerShakespeare.txt', 'Henry VIII': 'henry-viii_TXT_FolgerShakespeare.txt', 'Henry V': 'henry-v_TXT_FolgerShakespeare.txt', 'Julius Caesar': 'julius-caesar_TXT_FolgerShakespeare.txt', 'King John': 'king-john_TXT_FolgerShakespeare.txt', 'King Lear': 'king-lear_TXT_FolgerShakespeare.txt', "Love's Labor's Lost": 'loves-labors-lost_TXT_FolgerShakespeare.txt', 'Macbeth': 'macbeth_TXT_FolgerShakespeare.txt', 'Measure for Measure': 'measure-for-measure_TXT_FolgerShakespeare.txt', 'Much Ado About Nothing': 'much-ado-about-nothing_TXT_FolgerShakespeare.txt', 'Othello': 'othello_TXT_FolgerShakespeare.txt', 'Pericles, Prince of Tyre': 'pericles_TXT_FolgerShakespeare.txt', 'Richard III': 'richard-iii_TXT_FolgerShakespeare.txt', 'Richard II': 'richard-ii_TXT_FolgerShakespeare.txt', 'Romeo and Juliet': 'romeo-and-juliet_TXT_FolgerShakespeare.txt', 'The Comedy of Errors': 'the-comedy-of-errors_TXT_FolgerShakespeare.txt', 'The Merchant of Venice': 'the-merchant-of-venice_TXT_FolgerShakespeare.txt', 'The Merry Wives of Windsor': 'the-merry-wives-of-windsor_TXT_FolgerShakespeare.txt', 'The Phoenix and Turtle': 'the-phoenix-and-turtle_TXT_FolgerShakespeare.txt', 'The Taming of the Shrew': 'the-taming-of-the-shrew_TXT_FolgerShakespeare.txt', 'The Tempest': 'the-tempest_TXT_FolgerShakespeare.txt', 'The Two Gentlemen of Verona': 'the-two-gentlemen-of-verona_TXT_FolgerShakespeare.txt', 'The Two Noble Kinsmen': 'the-two-noble-kinsmen_TXT_FolgerShakespeare.txt', "The Winter's Tale": 'the-winters-tale_TXT_FolgerShakespeare.txt', 'Timon of Athens': 'timon-of-athens_TXT_FolgerShakespeare.txt', 'Titus Andronicus': 'titus-andronicus_TXT_FolgerShakespeare.txt', 'Troilus and Cressida': 'troilus-and-cressida_TXT_FolgerShakespeare.txt', 'Twelfth Night': 'twelfth-night_TXT_FolgerShakespeare.txt'} 
import re

def highlight_text(content, keyword):
    escaped_keyword = re.escape(keyword)
    pattern = re.compile(f'({escaped_keyword})', re.IGNORECASE | re.DOTALL)
    highlighted_content = pattern.sub(
        r'<span class="highlight" id="highlighted-line">\1</span>', content
    )
    return highlighted_content


@view_bp.route("/<title>/<sentence>")
def start(title, sentence):
  filename = title_to_filename[title]

  corpus_dir = os.path.join(current_app.root_path, 'corpus')
  file_path = os.path.join(corpus_dir, filename)

  with open(file_path, 'r') as file:
      content = file.read()

  content = highlight_text(content, sentence)
  
  return render_template('view.html', title=title, content=content, sentence = sentence)
