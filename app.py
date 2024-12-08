
from flask import Flask, request, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask_wtf.csrf import CSRFProtect
from objective import ObjectiveTest
from subjective import SubjectiveTest


app = Flask(__name__)
app.secret_key = 'aica2'
csrf = CSRFProtect(app)

class TestForm(FlaskForm):
    itext = TextAreaField('Input Text', validators=[DataRequired()])
    test_type = SelectField('Select Test Type', choices=[('objective', 'Objective'), ('subjective', 'Subjective')], validators=[DataRequired()])
    noq = IntegerField('Number of Questions', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Generate Test')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TestForm()
    if form.validate_on_submit():
        inputText = form.itext.data
        testType = form.test_type.data
        noOfQues = form.noq.data
        if testType == "objective":
            objective_generator = ObjectiveTest(inputText, noOfQues)
            question_list, answer_list = objective_generator.generate_test()
            testgenerate = zip(question_list, answer_list)
            return render_template('generatedtestdata.html', cresults=testgenerate)
        elif testType == "subjective":
            subjective_generator = SubjectiveTest(inputText, noOfQues)
            question_list, answer_list = subjective_generator.generate_test()
            testgenerate = zip(question_list, answer_list)
            return render_template('generatedtestdata.html', cresults=testgenerate)
        else:
            flash('Error Occurred!')
            return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
