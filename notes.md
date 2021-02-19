Overall code is quite clean -- especially in the backend -- frontend, would just 
delete what is commented out, and separate functions into a separate file. Comments below.

1. In hotel_builder, can clean up some of the code.
  # Location builder
  first do 
    hotel_json = hotel_details['hotel']

  and then can reference in code below
        lon = hotel_details['hotel']['longitude']
        lat = hotel_details['hotel']['latitude']
        address = hotel_details['hotel']['address']['lines'][0]

  first do 
    hotel_offer = hotel_details['offers'][0]
    and then reference below.
        offer_id = hotel_details['offers'][0]['id']
        check_in = hotel_details['offers'][0]['checkInDate']
        check_out = hotel_details['offers'][0]['checkOutDate']

2. Nice tests for the adapters, but add them for the models, and finish up that the builder builds an object.

3. In the frontend, move the functions to a separate file within the frontend folder, and then import.
Write tests for those functions (eg. name_to_id, find_hotel_by_id, etc.)
