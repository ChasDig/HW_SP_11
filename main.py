from flask import Flask, render_template
import untils


# Flask - class instance
app = Flask(__name__)


@app.route("/")
def candidate_list():
    return render_template('list.html')


@app.route("/candidate/AdelaHendricks.html/")
@app.route("/candidate/Adela Hendricks.html/")
def candidate_AdelaHendricks():
    candidate = untils.get_candidate_name('Adela Hendricks')
    return render_template('single.html', name=candidate[0]['name'], position=candidate[0]['position'], skills=candidate[0]['skills'], picture=candidate[0]['picture'])


@app.route("/candidate/Sheri Torres.html/")
@app.route("/candidate/SheriTorres.html/")
def candidate_SheriTorres():
    candidate = untils.get_candidate_name('Sheri Torres')
    return render_template('single.html', name=candidate[0]['name'], position=candidate[0]['position'], skills=candidate[0]['skills'], picture=candidate[0]['picture'])


@app.route("/candidate/Burt Stein.html/")
@app.route("/candidate/BurtStein.html/")
def candidate_BurtStein():
    candidate = untils.get_candidate_name('Burt Stein')
    return render_template('single.html', name=candidate[0]['name'], position=candidate[0]['position'], skills=candidate[0]['skills'], picture=candidate[0]['picture'])


@app.route("/candidate/Bauer Adkins.html/")
@app.route("/candidate/BauerAdkins.html/")
def candidate_BauerAdkins():
    candidate = untils.get_candidate_name('Bauer Adkins')
    return render_template('single.html', name=candidate[0]['name'], position=candidate[0]['position'], skills=candidate[0]['skills'], picture=candidate[0]['picture'])


@app.route("/candidate/Day Holloway.html/")
@app.route("/candidate/DayHolloway.html/")
def candidate_DayHolloway():
    candidate = untils.get_candidate_name('Day Holloway')
    return render_template('single.html', name=candidate[0]['name'], position=candidate[0]['position'], skills=candidate[0]['skills'], picture=candidate[0]['picture'])


@app.route("/candidate/Austin Cochran.html/")
@app.route("/candidate/AustinCochran.html/")
def candidate_AustinCochran():
    candidate = untils.get_candidate_name('Austin Cochran')
    return render_template('single.html', name=candidate[0]['name'], position=candidate[0]['position'], skills=candidate[0]['skills'], picture=candidate[0]['picture'])


@app.route("/candidate/Sheree Love.html/")
@app.route("/candidate/ShereeLove.html/")
def candidate_ShereeLove():
    candidate = untils.get_candidate_name('Sheree Love')
    return render_template('single.html', name=candidate[0]['name'], position=candidate[0]['position'], skills=candidate[0]['skills'], picture=candidate[0]['picture'])


@app.route("/search/<candidate_name>/")
def search_candidate(candidate_name):
    candidate = untils.search_candidate(str(candidate_name))
    return render_template('search.html', result=candidate)


@app.route("/skill/<skill_name>/")
def search_skills(skill_name):
    candidate = untils.search_candidate_skill(str(skill_name.lower()))
    return render_template('skill.html', result=candidate, skill_name=skill_name, address=untils.candidate_list)


if __name__ == "__main__":
    app.run(debug=True)
