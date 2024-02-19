function calculateShipping() {
  var weight = parseFloat(document.getElementById("weight").value);
  var distance = parseFloat(document.getElementById("distance").value);
  var method = document.getElementById("method").value;
  var shippingCost;

  if (isNaN(weight) || isNaN(distance)) {
      alert("Please enter valid numbers for weight and distance.");
      return;
  }

  if (method === "standard") {
      shippingCost = weight * 0.5 * distance;
  } else if (method === "expedited") {
      shippingCost = weight * 1.0 * distance + 5.0;
  }

  document.getElementById("result").innerHTML = "Shipping cost: $" + shippingCost.toFixed(2);
}
