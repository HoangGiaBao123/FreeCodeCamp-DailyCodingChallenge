function getGreeting(time) {
  const hours = parseInt(time.split(":")[0]);
  if(hours >= 22 || hours < 5) {
    return "Good night";
  } 
  if(hours >= 18 && hours < 22) {
    return "Good evening";
  }
  if(hours >= 12 && hours < 18) {
    return "Good afternoon";
  }
  if(hours >= 5 && hours < 12) {
    return "Good morning";
  }
}
