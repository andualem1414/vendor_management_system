# Vendor Management System 
 This system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics.

## Installation

  1. Install Pipenv
```bash
pip install pipenv
```
  3. Clone and navigate to the project folder
  4. Then run the command
```bash
pipenv install
```
  5. Then navigate to `vms` and run
```bash
python manage.py runserver
```
## Usage
Before you test, get your access token and refresh token at

  - `POST /api/user/token/ with`
  ```bash
{
      "username": "andu",
      "password": "admin123"
}

```
      
INCLUDE ACCESS TOKEN ON EVERY REQUEST

Or, Delete db.sqlite3 run `python manage.py makemigrations` and createsuperuser

## API documentation
### Vendor
  - `POST /api/vendors/`    Create a new vendor.
```bash
{
    "name": {vendor_name},
    "contact_details": {contact details},
    "address": {address}
}
```
  - `GET /api/vendors/`     List all vendors.
  - `GET /api/vendors/{vendor_id}/`                    Retrieve a specific vendor's details.
  - `PUT /api/vendors/{vendor_id}/update/`              Update a vendor's details.
  - `DELETE /api/vendors/{vendor_id}/delete/`           Delete a vendor.

### Purchase Order
  - `POST /api/purchase_orders/`                       Create a purchase order.
```bash
{
    "vendor": {vendor_id},
    "order_date": {order_date},
    "delivery_date": {delivery_date},
    "items": {item list},
    "quantity": {quantity},
    "status": {choice between COMPLETED, PENDING, CANCELED},
    "quality_rating": {rating},
    "issue_date": {issue_date}
}
```
  - `POST /api/purchase_orders/{po_id}/acknowledge/`     Acknowledge a purchase order
  - `GET /api/purchase_orders/`                        List all purchase orders.
  - `GET /api/purchase_orders/?vendor_id={id}`         List all purchase orders that belong to the vendor.
  - `GET /api/purchase_orders/{po_id}/`               Retrieve details of a specific purchase order.
  - `PUT /api/purchase_orders/{po_id}/update/`         Update a purchase order.
  - `DELETE /api/purchase_orders/{po_id}/delete/`     Delete a purchase order.
  


Performance Metrics
  - `GET /api/vendors/{vendor_id}/performance/`        Retrieve Performance metrics for a vendor
```bash
{
    "id": 3,
    "date": "2024-04-30T17:10:05.821995Z",
    "on_time_delivery_rate": 0.0,
    "quality_rating_avg": 9.0,
    "average_response_time": 808361.0,
    "fullfillment_rate": 0.33,
    "vendor": 5
}
``` 




