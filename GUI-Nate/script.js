const cinp = cinpBuilder( "http://localhost:8888" );

function setupBackend() {
  cinp.describe( "/api/v1/" ).done(
    function( resp ) {
      if( resp.version != "1.0" ) {
        alert( "Invalid API version" );
        return;
      }
      login();
    } ).fail( function() { alert( "unable to find backend" ); } );
}

function login() {
  cinp.call("/api/v1/Auth/User(login)", { "username": "ui", "password": "ui" } ).done(
    function( resp ) {
      cinp.setAuth( "ui", resp );
    } ).fail(
    function( resp ) {
      alert( "failed to authencate to the backend" );
    } );
}

function login_via_camera() {
  cinp.call("/api/v1/Auth/User(login_via_camera)", {} ).done(
    function( resp ) {
      cinp.setAuth( "__Customer__", resp );
    } ).fail(
    function( resp ) {
      alert( "failed to authencate with camera" );
    } );
}

async function get_customer_info() {
  const customer_uri = await cinp.call("/api/v1/Auth/User(customer)", {} );

  return await cinp.get( customer_uri );
}

function doAlert( msg ) {
  alert( msg );
}

function getGroupsArr() {
  return new Promise((resolve, reject) => {
    let products = [];
    cinp.getFilteredObjects("/api/v1/Products/ProductGroup").done(function(resp) {
      let groupArray = {};
      for (const [uri, name] of Object.entries(resp)) {
        groupArray[uri] = name;
      }
      resolve(products);
    }).fail(function() {
      reject("Unable to get product list");
    });
  });
}

function getProductsArr() {
  return new Promise((resolve, reject) => {
    let products = [];
    cinp.getFilteredObjects("/api/v1/Products/Product").done(function(resp) {
      for (const [uri, product] of Object.entries(resp)) {
        let productArray = [
          product.name,
          product.cost,
          product.location,
          product.available,
          product.id,
          product.group,
          uri
        ];
        products.push(productArray);
      }
      resolve(products);
    }).fail(function() {
      reject("Unable to get product list");
    });
  });
}

async function showInfo(button) {
  const infoSpot = $("#info");
  try {
    let products = await getProductsArr();
    const productLocation = button.textContent;
    for (let i = 0; i < products.length; i++) {
      if (products[i][2] === productLocation) {
        infoSpot.empty();
        infoSpot.append(`
          <div>The price of the ${products[i][0]} is $${products[i][1]} there are ${products[i][3]} available.</div>
          <button class="button" onclick="buy('${products[i][0]}', ${products[i][1]}, '${products[i][2]}', ${products[i][3]}, ${products[i][4]})">Buy</button>
        `);
      }
    }
  } catch (error) {
    infoSpot.empty();
    infoSpot.append(`<div>${error}</div>`);
  }
}

async function selectGroup() {
  const infoSpot = $("#grid");
  try {
    let groups = await getGroupsArr();
    const productLocation = button.textContent;
    infoSpot.empty();
    for (const uri in groups) {
      
        infoSpot.append(`
          <button class="button">${groups[uri]}</button>
        `);
    }
  } catch (error) {
    infoSpot.empty();
    infoSpot.append(`<div>${error}</div>`);
  }
}

//<button class="button" onclick="buy('${products[i][0]}', ${products[i][1]}, '${products[i][2]}', ${products[i][3]}, ${products[i][4]})">Buy</button>

function buy(product, price, location, available, id) {
  const infoSpot = $("#info");
  infoSpot.empty();
  infoSpot.append(`
    <div>You have successfully bought the ${product} for a total of $${price}. </br>Please end your transaction to purchase another item.</div>
    <button class="button" onclick="end()">End</button>
  `);

}

function end() {
  const infoSpot = $("#info");
  infoSpot.empty();
}

function showAlert(button) {
  alert(button.textContent + " button clicked");
}

setupBackend();
