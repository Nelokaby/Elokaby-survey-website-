from flask import Flask, render_template, request

app = Flask(__name__)

def questions_data():
    questions = {
        "الاسم":[],
        "السن":[],
        "(BMI)معدل الوزن مقارنة بالطول":[],
        'هل يوجد أمراض؟': ['حمل', 'رضاعة', 'أمراض مزمنة', 'لا يوجد'],
        "معدل الحرق":[],
        "مشكلة الوزن": ['نحافة', 'زيادة في الوزن','لا يوجد'],
        "مشكلة الشعر":["تقصف ونعومة","انبات","لا يوجد مشاكل"],
        "مشكلة الوجه":["هالات","حبوب","تصبغات وندبات","لا يوجد"],
        "مشكلة المناطق الحساسة":["غمقان","شعر تحت الجلد","لا يوجد"],
        "مشكلة المناطق الغير حساسة":["غمقان(الكوع/الركبة)","جلد وزة","تشققات","لا يوجد"],
        "مشاكل اخرى":["رموش","حواجب","شفايف","اسنان",'لا يوجد']
    }
    return questions

def answers_data():
    
    inbat = """ استخدام تركيبة غنية بالفيتامينات الفعالة في إنبات الشعر مرة اخري وفيتامينات مثل الاوميجا ثري والجينكوبيلوبا والقيام بالتحاليل المناسبة كالسيوم وهيموجلوبين مخزون الحديد"""
    tqasof=""" استخدام حمام كريم للترطيب وفرد الكسر وشامبو غني بالارجان والجوجوبا وكريم للترطيب وعلاج التقصف"""

    halat="إستخدام كريم للترطيب وتفتيح تحت العين وجهاز مساج لزيادة الدورة الدموية تحت العين مع هيالورونيك اسيد لزيادة النضارة ومنع التجاعيد مع تقليل المنبهات والنوم ثمان ساعات وزيادة شرب المياه"
    hobob= " استخدام مضادات للبكتيريا والالتهابات وعلاج ندبات الحبوب بمنتجات طبيعية واستخدام ماسك لتنضيف المسام وقفلها وإزالة البثور"
    nadabat="بعد ما بنتخلص من اي حبوب في بشرتنا بيفضل فيها ندبات و تصبغات بتقلل من جمال مظهرها .. صيدليات العقبي بتوفرلك كريمات طبيعية لتفتيح التصبغات والندبات مع ماسك لقفل المسام وإزالة البثور"

    ghamaqan_1="استخدام كريمات طبيعية لتفتيح وإفراز الكولاجين الطبيعي وتقليل إفراز الميلانين وتنضيف المسام وتقليل ريحة العرق"
    shaar_t7t_elgeld_1="الشعر تحت الجلد بيأثر على مظهر البشرة و ملمسها و احيانا بيسبب حبوب والتهابات .. صيدليات العقبي بتوفرلك منتجات طبيعية لإزالة الشعر تحت الجلد مع تنعيم المنطقة وتقليل ريحة العرق"

    ghamaqan_2="لمشاكل المناطق الغير حساسة صيدليات العقبي بتوفر منتجات طبيعية لتفتيح وتنعيم وتقليل التصبغات وإزالة الشعر تحت الجلد والجلد الميت"

    romosh="استخدام سيرم طبيعي لزيادة إنبات الرموش وتطويلها وتكثيفها"
    hawageb="استخدام سيرم طبيعي لزيادة إنبات الحواجب وتطويلها وتكثيفها"
    shafayef="استخدام منتجات طبيعية لإزالة الجلد الميت والترطيب والتنعيم"
    asnan=" إزالة الجير بمواد طبيعية للحفاظ علي طبقة مينا الأسنان من التآكل واللي بتحمي الأسنان من التسوس ومن حساسية الأسنان"

    answers= {
        "نحافة":" إستخدام مجموعة علاج النحافة وهي خالية تماما من الكورتيزون و اي مواد ضارة لصحتك و غنية بالفيتامينات والبروتينات اللي بتعوض نقصهم في جسمك و بتساعدك تبنيه صح ... هنا هنساعدك تزودي وزنك و كمان تزودي ثقتك بنفسك",
        'زيادة في الوزن':" إستخدام تركيبة التخسيس اللي بتسد النفس و تزود الحرق وكمان بنخلي دكتور يتابع معاكي و يعملك نظام غذائي مخصوص علشانك لحد ما نوصل للجسم المثالي ليكي و معاها سكر دايت مبيغيرش طعم المشروبات و مفيهوش سعرات حرارية",
        "تقصف ونعومة":tqasof,
        "انبات":inbat,
        "هالات":halat,
        "حبوب":hobob,
        "تصبغات وندبات":nadabat,
        "غمقان":ghamaqan_1,
        "شعر تحت الجلد":shaar_t7t_elgeld_1,
        "جلد وزة":ghamaqan_2,
        "تشققات":ghamaqan_2,
        "غمقان(الكوع/الركبة)":ghamaqan_2,
        "رموش":romosh,
        "حواجب":hawageb,
        "شفايف":shafayef,
        "اسنان":asnan,
        "لا يوجد":"",
        "لا يوجد مشاكل":"",
        'حمل':"", 'رضاعة':"", 'أمراض مزمنة':""

    }

    return answers
@app.route('/')
def survey():
    questions = questions_data()
    return render_template('index.html',questions=questions)


@app.route('/submit', methods=["Get",'post'])
#@app.route("/result ", methods= ["Get","Post"])
def result():
    questions=questions_data()
    opposite_data= [
        'هل يوجد أمراض؟',
        "مشكلة الوزن",
        "مشكلة الشعر",
        "مشكلة الوجه",
        "مشكلة المناطق الحساسة",
        "مشكلة المناطق الغير حساسة",
        "مشاكل اخرى"
    ]
    data= request.form.to_dict("utf-8")   
    for key in questions.keys():
        if key in opposite_data:
            data[key]=request.form.getlist(key)

    dict_rate={
        'هل يوجد أمراض؟':[0,0,0,0],
        "مشكلة الوزن": [-1,-1,0],
        "مشكلة الشعر":[-1,-1,0],
        "مشكلة الوجه":[-1,-1,-1,0],
        "مشكلة المناطق الحساسة":[-1,-1,0],
        "مشكلة المناطق الغير حساسة":[-1,-1,-1,0],
        "مشاكل اخرى":[-1,-1,-1,-1,0]
    }

    
    rate=15
    answers=answers_data()

    for question , answer in data.items():
        prob={}
        if (question in opposite_data) :
            if type(answer)==list and question == 'هل يوجد أمراض؟': 
                data[question]=' - '.join(map(str, answer))
            elif type(answer)==list and question == "مشكلة المناطق الغير حساسة":
                if "لا يوجد" not in answer and len(answer)>0:
                    temp=" - ".join(map(str,answer))
                    prob[temp]=answers[answer[0]]
                    for item in answer:
                        i=questions[question].index(item)
                        rate=rate+dict_rate[question][i]
                else:
                    prob["لا يوجد"]=answers["لا يوجد"]
                data[question]=prob
            elif type(answer)==list :
                for item in answer:
                    prob[item]=answers[item]
                    i=questions[question].index(item)
                    rate=rate+dict_rate[question][i]
                    data[question]=prob
            else:
                prob[answer]=answers[answer]
                i=questions[question].index(answer)
                rate=rate+dict_rate[question][i]
                data[question]=prob


    return render_template("result.html", questions=data,rate=rate )

if __name__ == '__main__':
    app.run()


