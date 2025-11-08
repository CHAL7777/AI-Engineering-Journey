<?php

// $gpa=86;

// if($gpa>85){
//     echo "you have sscored A excellent";
// }
// elseif($gpa>90){
//     echo "wow ammazing you have scored a charge kudos";
// }
// else{
//     echo "sorry you have to improve you grade";
// }
// for($i=0;$i<=20;$i++){
//     if($i%2==0){
//         echo "$i is even number";
//         echo "<br>";
//     }
// }


// 1. Define the Quiz (Using an Array of Arrays)
$quizQuestions = [
    ["question" => "What is the capital of France?", "answer" => "Paris"],
    ["question" => "Which planet is known as the Red Planet?", "answer" => "Mars"],
    ["question" => "What is 2 + 2?", "answer" => "4"],
    // Add 2 more questions of your choice!
];

// 2. Initialize the score
$score = 0;

// 3. Function to check the answer
function checkAnswer($userAnswer, $correctAnswer) {
    // Hint: Use strtolower() to make comparison case-insensitive
    return strtolower(trim($userAnswer)) == strtolower(trim($correctAnswer));
}

echo "Welcome to the Simple Quiz!\n";
echo "Please answer the following questions:\n\n";

// 4. Loop through each question
foreach ($quizQuestions as $index => $qna) {
    $questionNumber = $index + 1;
    echo "Question $questionNumber: " . $qna['question'] . "\n";

    // In a real web app, you'd use a form. Here we'll simulate answers.
    // For now, let's just assume the answers are hardcoded in an array.
    // A more advanced version would take user input.
    $simulatedUserAnswers = ["Paris", "Jupiter", "4"]; // One wrong answer
    $userAnswer = $simulatedUserAnswers[$index];

    echo "Your answer: $userAnswer\n";

    // 5. Check the answer and update the score
    if (checkAnswer($userAnswer, $qna['answer'])) {
        echo "Correct!\n";
        $score++;
    } else {
        echo "Wrong! The correct answer is: " . $qna['answer'] . "\n";
    }
    echo "------------------------\n";
}

// 6. Display the final result
$totalQuestions = count($quizQuestions);
$percentage = ($score / $totalQuestions) * 100;

echo "\n*** QUIZ COMPLETE! ***\n";
echo "Your final score is: $score/$totalQuestions ($percentage%)\n";

// 7. Give a message based on the score
if ($percentage == 100) {
    echo "Perfect! You are a genius!\n";
} elseif ($percentage >= 70) {
    echo "Well done!\n";
} elseif ($percentage >= 50) {
    echo "Good effort!\n";
} else {
    echo "Better luck next time!\n";
}


?>