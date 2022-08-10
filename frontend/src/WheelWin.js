import React from 'react'
import WheelComponent from 'react-wheel-of-prizes';

export default function WheelWin(props) {
  console.log(props.win)
  return (
    <WheelComponent
          segments={props.segment}
          segColors={props.color}
          winningSegment={props.win}
          onFinished={props.onFinished}
          primaryColor='#d4a961'
          contrastColor='#524126'
          buttonText="۵شانس"
          isOnlyOnce={false}
          size={250}
          upDuration={100}
          downDuration={1000}
          fontFamily='Arial'
        />
  )
}
