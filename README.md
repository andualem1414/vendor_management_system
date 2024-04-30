Vendor Management System 
To run
  1. Install Pipenv
  2. clone and navigate to the project folder
  3. then run the command:  pipenv install
  4. then run:  python manage.py runserver

Before you test, get your access token and refresh token at:
  ● POST /api/user/token/ with:
      {
        "username": "andu",
        "password": "admin123"
      }

INCLUDE ACCESS TOKEN ON EVERY REQUEST

Vendor
  ● POST /api/vendors/:                                Create a new vendor.
  ● GET /api/vendors/:                                 List all vendors.
  ● GET /api/vendors/{vendor_id}/:                     Retrieve a specific vendor's details.
  ● PUT /api/vendors/{vendor_id}/update/:              Update a vendor's details.
  ● DELETE /api/vendors/{vendor_id}/delete/:           Delete a vendor.

Purchase Order
  ● POST /api/purchase_orders/:                        Create a purchase order.
  ● POST /api/purchase_orders/{po_id}/acknowledge/     Acknowledge a purchase order
  ● GET /api/purchase_orders/:                         List all purchase orders.
  ● GET /api/purchase_orders/?vendor_id={id}:          List all purchase orders that belong to the vendor.
  ● GET /api/purchase_orders/{po_id}/:                 Retrieve details of a specific purchase order.
  ● PUT /api/purchase_orders/{po_id}/update/:          Update a purchase order.
  ● DELETE /api/purchase_orders/{po_id}/delete/:       Delete a purchase order.
  


Performance Metrics
  ● GET /api/vendors/{vendor_id}/performance/:         Retrieve Performance metrics for a vendor
  



  

