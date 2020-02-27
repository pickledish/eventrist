export function getTimeRange(offsetMs) {
  var now = Date.now();
  var then = now - offsetMs
  return [then, now]
}
