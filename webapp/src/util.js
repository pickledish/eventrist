export function getTimeRange(offsetMs) {
  var now = Date.now();
  var then = now - offsetMs
  return [then, now]
}

export function getOrElse(x, els) {
  return (x === undefined || x === null) ? els : x;
}
