import React, { useState } from "react";

function Visualize() {
  const [input1, setInput1] = useState("");
  const [input2, setInput2] = useState("");

  const handleChangeU = (e) => {
    setInput1(e.target.value);
  };
  const handleChangeR = (e) => {
    setInput2(e.target.value);
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(input1, input2);
    setInput1("");
    setInput2("");
  };
  return (
    <>
      <html lang="en" dir="ltr">
        <head>
          <title>fuck react</title>
        </head>
        <body>
          <div class="center">
            <div class="title">Github Details</div>
            <div class="sub_title">Get details about github repositories</div>
            <form class="form" onSubmit={handleSubmit}>
              <div class="btns">
                <input
                  type="text"
                  placeholder="Username"
                  value={input1}
                  onChange={handleChangeU}
                ></input>
                <input
                  type="text"
                  placeholder="Repository"
                  value={input2}
                  onChange={handleChangeR}
                ></input>
                <button>Search</button>
              </div>
            </form>
          </div>
        </body>
      </html>
    </>
  );
}

export default Visualize;
