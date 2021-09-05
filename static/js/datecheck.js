  function validateForm() {
    let subreddit = document.forms["myForm"]["subreddit"].value;
    let startdate = document.forms["myForm"]["startdate"].value;
    let enddate = document.forms["myForm"]["enddate"].value;
    var sd=new Date(startdate)
    var ed=new Date(enddate)
    console.log(startdate,enddate,sd,ed, sd >= ed)
    if (subreddit == "") {
      alert("subreddit must be filled out");
      return false;
    } else if (startdate == ""){
      alert("start date must be filled out");
      return false;
    } else if (enddate == ""){
      alert("end date must be filled out");
      return false;
    } else if (sd >= ed){
      alert("start date should be more less that end date")
      return false
    }
  }