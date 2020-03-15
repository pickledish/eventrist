export function getTimeRange(offsetMs) {
  var now = Date.now();
  var then = now - offsetMs
  return [then, now]
}

export function getOrElse(x, els) {
  return (x === undefined || x === null) ? els : x;
}

export function flatten(arr) {
	return arr.reduce((acc, val) => acc.concat(val), [])
}

export function getQueryParam(paramName, els) {
	let paramDict = new URL(document.location).searchParams;
	return getOrElse(paramDict.get(paramName), els);
}

export function setQueryParam(paramName, newValue) {
	let params = new URL(document.location).searchParams;
    params.set(paramName, newValue);
    window.history.pushState({}, "", "?" + params.toString())
}
