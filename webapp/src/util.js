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

export function getQueryParam(paramName, defaultValue) {
  let paramDict = new URL(document.location).searchParams;
  if (paramDict.has(paramName)) {
    let stringValue = paramDict.get(paramName)
    if (stringValue.includes(',')) {
      return stringValue.split(',')
    } else {
      return stringValue
    }
  } else {
    return defaultValue
  }
}

export function setQueryParam(paramName, newValue) {
  let params = new URL(document.location).searchParams;
  if (Array.isArray(newValue)) {
    if (newValue.length == 0) {
      params.delete(paramName);
    } else {
      params.set(paramName, newValue.join(','));
    }
  } else {
    params.set(paramName, newValue);
  }
  window.history.pushState({}, "", "?" + params.toString());
}
