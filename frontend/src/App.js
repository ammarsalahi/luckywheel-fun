import { useEffect, useState } from 'react';
import Api from './Api';
import 'bootstrap/dist/css/bootstrap.min.css';
import Swal from 'sweetalert2';
import 'font-awesome/css/font-awesome.min.css';
import WheelComponent from 'react-wheel-of-prizes';

function App() {
  
  const [segment, setsegment] = useState([])
  const [color, setcolor] = useState([])
  const [show, setshow] = useState(false);
  const [data, setdata] = useState([]);
  const [spacial, setspacial] = useState("");
  const [limit, setlimit] = useState(-1);
  const [hide, sethide] = useState("")
  let count=1

  useEffect(()=>{
        getData();
        getSpacialAward()
        getHideAward()
  },[]);
  
  const getData=()=>{
    Api.get('/award/').then(res=>{
      for(let i=0;i<res.data.length;i++){
        setdata(res.data)
      }
    });
  }
  const getSpacialAward=()=>{
    Api.get('/spacialaward/').then(res=>{
      for(let i=0;i<res.data.length;i++){
        setspacial(res.data[i].award)
        setlimit(res.data[i].count_number);
      }
    }).catch(err=>{
      setspacial("");
      setlimit(-1)
    });
  }
  const getHideAward=()=>{
    Api.get('/hideaward/').then(res=>{
      for(let i=0;i<res.data.length;i++){
        sethide(res.data[i].award)
      }
    }).catch(err=>{
      sethide("");
    });
  }
  const setDataToWheel=()=>{
    for(let i=0;i<data.length;i++){
        segment.push(data[i].text);
        color.push(data[i].color);
    }
    setshow(true)
  }
  const showAlert=(text,title)=>{
    Swal.fire({
      iconHtml:'<i class="fa fa-trophy text-warning" style="fontSize:100px" ></i>',
      title:title,
      html:' <div dir="rtl"><h2 className="text-success">'+text+'</h2></div>',
      confirmButtonText:'باشه',
      showConfirmButton:true
    });
  }
  const showAlertAward=(text)=>{
    Api.get('/award/'+text).then(res=>{
      Swal.fire({
        iconHtml:'<i class="fa fa-trophy text-warning" style="fontSize:100px" ></i>',
        html:' <div dir="rtl"><h2 className="text-success">'+res.data.award+'</h2></div>',
        confirmButtonText:'باشه',
        showConfirmButton:true
      });
    });
   
  }
  const onFinished = (winner) => {
    if(hide===""){
      if(count===limit){
        showAlert(spacial,'جایزه ویژه');
        count++;
      }else{
        showAlertAward(winner);
        count++;
      }
    }else{
      showAlert(hide,'');
    }
    
    
  }
 
  return (
      <div dir='rtl'>
      <center>
      {show ===false ?
       <div className='container' style={{paddingTop:"20%"}}>
        <button className='btn btn-lg btn-warning rounded-pill' onClick={setDataToWheel}>شانس خود را امتحان کنید</button>
      </div>:
      <WheelComponent
      segments={segment}
      segColors={color}
      onFinished={(winner)=> onFinished(winner)}
      primaryColor='#d4a961'
      contrastColor='#524126'
      buttonText="بچرخ"
      isOnlyOnce={false}
      size={250}
      upDuration={100}
      downDuration={1000}
      fontFamily='Arial'
    />
      }
      </center>
    
      
    </div>
  );

}

export default App;