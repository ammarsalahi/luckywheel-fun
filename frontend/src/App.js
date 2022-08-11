import { useEffect, useState } from 'react';
import Api from './Api';
import 'bootstrap/dist/css/bootstrap.min.css';
import Swal from 'sweetalert2';
import WheelComponent from 'react-wheel-of-prizes';
import 'font-awesome/css/font-awesome.min.css';

function App() {
  
  const [segment, setsegment] = useState([])
  const [color, setcolor] = useState([])
  const [show, setshow] = useState(false);
  const [data, setdata] = useState([]);
  const [isload,setisload]=useState(true);
  const [win, setWin] = useState("");
  useEffect(()=>{
    if(isload==true){
      getData();
      getActiveData() 
      setisload(false)
    }
       
  },[]);
  
  const getData=()=>{
    Api.get('/luckyaward/').then(res=>{
      for(let i=0;i<res.data.length;i++){
        setdata(res.data)
      }
      if(res.data.length===0){
        setisload(true);
      }
    }).catch(err=>{
       setisload(true);
    });
  }
  const getActiveData=()=>{
    Api.get('/award/').then(res=>{
      console.log(res.data.award)
      setWin(res.data.award);
      
    }).catch(err=>{
      setWin("");
    });
  }
  const setDataToWheel=()=>{
    for(let i=0;i<data.length;i++){
        segment.push(data[i].text);
        color.push(data[i].color);
    }
    setshow(true)
  }
 
  const showAlert=(text)=>{
    Api.get('/luckyaward/'+text).then(res=>{
      Swal.fire({
        iconHtml:'<i class="fa fa-trophy text-warning" style="fontSize:100px" ></i>',
        html:' <div dir="rtl"><h2 className="text-success">'+res.data.award+'</h2></div>',
        confirmButtonText:'باشه',
        showConfirmButton:true
      });
    });
   
  }
  const onFinished = (winner) => {
    showAlert(winner)
  }
  return (
      <div dir='rtl'>
      <center>
      {show ===false ?
       <div className='container' style={{paddingTop:"20%"}}>
       
        <button className='btn btn-lg btn-warning rounded-pill' disabled={isload} onClick={setDataToWheel}>شانس خود را امتحان کنید</button>
      </div>:
       <WheelComponent
       segments={segment}
       segColors={color}
       winningSegment={win}
       onFinished={(winner)=>{onFinished(winner)}}
       primaryColor='#000000'
       contrastColor='#ffffff'
       buttonText="بچرخ"
       isOnlyOnce={true}
       size={250}
       upDuration={1000}
       downDuration={10000}
       fontFamily='Arial'
       />
      }
      
      </center>
    
      
    </div>
  );

}

export default App;
