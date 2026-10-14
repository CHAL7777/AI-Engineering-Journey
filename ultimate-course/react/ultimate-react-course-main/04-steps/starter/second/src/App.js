import { useState } from "react";






const messages = [
  "Learn React ⚛️",
  "Apply for jobs 💼",
  "Invest your new income 🤑",
];
export default function App(){
  return <div>
    <Steps/>
     <Steps/>
  </div>
}

 function Steps(){
  const [step,setStep]=useState(1)
   function pre(){
      if(step>1){
        setStep((s)=>s-1);
        console.log(setStep);
        console.log(step);
        
      }
    }
    function next(){
      if(step<3){
        setStep((s)=>s+1);
      }
    }
    
  return <div className="steps">

   
    <div className="numbers">
      <div className={`${step>=1?"active":""}`}>1</div>
       <div className={`${step>=2?"active":""}`}>2</div>
        <div className={`${step>=3?"active":""}`}>3</div>
    </div>
    <p className="message">step : {step} {messages[step-1]}</p>
    <div className="buttons ">
      <button style={{backgroundColor:"#7950f2",color:"#fff"}} onClick={pre}>previous</button>
      <button style={{backgroundColor:"#7950f2",color:"#fff"}} onClick={next}>next</button>
    </div>
  </div>
}


// export default function App(){
//  const [step,setStep]=useState(1);
//   function handlerP(){
//    if(step>1){
//     setStep(step-1)
//    }
//   }
//   function handlerN(){
//     if(step<3){
//       setStep(step+1)
//     }
//   }
//   return <div className="steps">
//     <div className="numbers">
//       <div className={`${step>=1?"active":""}`}>1</div>
//       <div className={`${step>=2?"active":""}`}>2</div>
//       <div className={`${step>=3?"active":""}`}>3</div>
//     </div>
//     <p className="message">Step {step} : {messages[step-1]} </p>
//     <div className="buttons">
//       <button style={{backgroundColor:"#7950f2",color:"#fff"}} onClick={handlerP}>previous</button>
//        <button style={{backgroundColor:"#7950f2",color:"#fff"}} onClick={handlerN} >next</button>
//     </div>
//   </div>
// }