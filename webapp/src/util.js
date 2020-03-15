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

export function getQueryParam(paramName, defualt) {
	let paramDict = new URL(document.location).searchParams;
	console.log(paramDict.get(paramName))
	return getOrElse(paramDict.get(paramName), defualt);
}
