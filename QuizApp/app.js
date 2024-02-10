const quiz =[
    {
        question : 'ジョルノ・ジョバーナのスタンド名は？',
        answers  : [
            'ゴールドエクスペリエンス',
            'ストーンフリー',
            'スタープラチナ',
            'クレイジーダイヤモンド'
        ],
        correct  :  'ゴールドエクスペリエンス'
    },

    {
        question : 'ジョルノ・ジョバーナが所属する組織の名前は？',
        answers  : [
            'ヒットマンチーム',
            'スピードワゴン財団',
            'グリーンドルフィン',
            'パッショーネ',
        ],
        correct  :  'パッショーネ'
    },

    {
        question : 'パッショーネのボスの名前は？',
        answers  : [
            'ポルポ',
            'ブチャラティ',
            'ディアボロ',
            'キング・クリムゾン',
        ],
        correct  :  'ディアボロ'
    },
];

const quizLength = quiz.length ;
let quizIndex = 0 ;
let score = 0;

//HTMLのタグを取得してる場合は$をつける
const $button = document.getElementsByTagName('button');
const buttonLength = $button.length;


//問題文とボタンの定義
const setupQuiz = () => {
    //問題文
    document.getElementById('js-question').textContent=quiz[quizIndex].question;
    //ボタン表示
    let buttonIndex = 0;
    //ボタンの配列から数を取得するために定義

    //最初に定義したbuttonIndexが配列数以内に収まっている限り、クリックするごとに+1
    while( buttonIndex < buttonLength ){
        $button[buttonIndex].textContent=quiz[quizIndex].answers[buttonIndex];
        buttonIndex++;
    };
};

setupQuiz();

const clickHandler = (e) =>{
    if(quiz[quizIndex].correct === e.target.textContent){
        window.alert('正解ッッ！');
        //正解したら加点
        score++;
    }
    else{
        window.alert('不正解ッッ...');
    }

    quizIndex++;
    //問題数ありの場合の命令
    if(quizIndex < quizLength){
        setupQuiz();
    }
    //問題数なしの場合の命令
    else{
        window.alert('終了ッッ！君のスコアは'+ score + 'だッッ');
        location.href= 'C:/Users/Marina%20Inoue/Desktop/practice/QuizApp/finishpage.html';
    }
};



//正解不正解の判断//
//1:34:50~
let handlerIndex = 0;
while( handlerIndex < buttonLength){
    $button[handlerIndex].addEventListener('click',(e)=>{
        clickHandler(e);
    });
    handlerIndex++;
};

