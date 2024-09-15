import webbrowser

f=open("1.html","w") #creates a file, if it's not sure it already exists
message = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Angi Scraper</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
  <style>
    body {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      height: 100vh;
      background-color: #222;
      font-family: "Roboto", sans-serif;
    }

    h1 {
      text-align: center;
      color: #fff;
      margin-bottom: 100px;
    }
    .formtab{
      max-width:500px;
      margin:auto;
    }
    label {
      display: block;
      margin-bottom: 5px;
      color: #fff;
    }
    select, select option{
      color:#000;
    }
    input {
      margin-bottom: 10px;
      background-color: #fff;
      color: #333;
      border: 1px solid #444;
      width:100%;
    }

    button {
      background-color: #fff;
      color: #333;
      border: none;
      padding: 10px 20px;
      cursor: pointer;
    }
    #loader {
      border: 8px solid #f3f3f3; /* Light grey */
      border-top: 8px solid #3498db; /* Blue */
      border-radius: 50%;
      width: 50px;
      height: 50px;
      animation: spin 1s linear infinite;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

  </style>
</head>
<body>
<div class="formtab">
  <h1>Angi Business Scraper</h1>
    <form action="/scrape" method="POST" id="myForm">
      <p><label for="category">Category:</label></p>
      <select name="catg" id="catg" style="width: 100%;>
        <option value="Air Duct Cleaning">Air Duct Cleaning</option>
        <option value="Animal Removal">Animal Removal</option>
        <option value="Antenna Repair">Antenna Repair</option>
        <option value="Appliance Repair">Appliance Repair</option>
        <option value="Architect">Architect</option>
        <option value="Asbestos Removal">Asbestos Removal</option>
        <option value="Awnings">Awnings</option>
        <option value="Basement Remodeling">Basement Remodeling</option>
        <option value="Basement Waterproofing">Basement Waterproofing</option>
        <option value="Basketball Hoop Installation">Basketball Hoop Installation</option>
        <option value="Bathtub Refinishing">Bathtub Refinishing</option>
        <option value="Biohazard Cleanup">Biohazard Cleanup</option>
        <option value="Blind Cleaning">Blind Cleaning</option>
        <option value="Cabinet Makers">Cabinet Makers</option>
        <option value="Cabinet Refacing">Cabinet Refacing</option>
        <option value="Carpet Cleaning">Carpet Cleaning</option>
        <option value="Carpet Installation">Carpet Installation</option>
        <option value="Ceiling Fan Installation">Ceiling Fan Installation</option>
        <option value="Central Vacuum Cleaning">Central Vacuum Cleaning</option>
        <option value="Childproofing">Childproofing</option>
        <option value="Chimney Cap Repair">Chimney Cap Repair</option>
        <option value="Chimney Repair">Chimney Repair</option>
        <option value="Chimney Sweep">Chimney Sweep</option>
        <option value="Cleaning Services">Cleaning Services</option>
        <option value="Closet Design">Closet Design</option>
        <option value="Computer Repair">Computer Repair</option>
        <option value="Concrete Driveways">Concrete Driveways</option>
        <option value="Concrete Repair">Concrete Repair</option>
        <option value="Countertop Installation">Countertop Installation</option>
        <option value="Deck Cleaning">Deck Cleaning</option>
        <option value="Decks & Porches">Decks & Porches</option>
        <option value="Dock Building">Dock Building</option>
        <option value="Dog Fencing">Dog Fencing</option>
        <option value="Door Installation">Door Installation</option>
        <option value="Drain Cleaning">Drain Cleaning</option>
        <option value="Drain Pipe Installation">Drain Pipe Installation</option>
        <option value="Drapery Cleaning">Drapery Cleaning</option>
        <option value="Driveway Gate Installation">Driveway Gate Installation</option>
        <option value="Driveway Pavers">Driveway Pavers</option>
        <option value="Dryer Vent Cleaning">Dryer Vent Cleaning</option>
        <option value="Drywall">Drywall</option>
        <option value="Dumpster Rental">Dumpster Rental</option>
        <option value="Earthquake Retrofitting">Earthquake Retrofitting</option>
        <option value="Egress Window">Egress Window</option>
        <option value="Electrician">Electrician</option>
        <option value="Epoxy Flooring">Epoxy Flooring</option>
        <option value="Excavating">Excavating</option>
        <option value="Fence Company">Fence Company</option>
        <option value="Fireplace Services">Fireplace Services</option>
        <option value="Firewood Company">Firewood Company</option>
        <option value="Floor Buffing">Floor Buffing</option>
        <option value="Floor Cleaning">Floor Cleaning</option>
        <option value="Flooring">Flooring</option>
        <option value="Foundation Repair">Foundation Repair</option>
        <option value="Fountains">Fountains</option>
        <option value="Furniture Refinishing">Furniture Refinishing</option>
        <option value="Garage Building">Garage Building</option>
        <option value="Garage Doors">Garage Doors</option>
        <option value="Gas Fireplace Repair">Gas Fireplace Repair</option>
        <option value="Gas Leak Repair">Gas Leak Repair</option>
        <option value="General Contractors">General Contractors</option>
        <option value="Generator Service">Generator Service</option>
        <option value="Glass Block">Glass Block</option>
        <option value="Glass Repair">Glass Repair</option>
        <option value="Grill Repair">Grill Repair</option>
        <option value="Gutter Cleaning">Gutter Cleaning</option>
        <option value="Gutter Repair">Gutter Repair</option>
        <option value="Handyman">Handyman</option>
        <option value="Hardscaping">Hardscaping</option>
        <option value="Hardwood Floors">Hardwood Floors</option>
        <option value="Hauling">Hauling</option>
        <option value="Heating Oil Company">Heating Oil Company</option>
        <option value="Holiday Decorating">Holiday Decorating</option>
        <option value="Home Automation">Home Automation</option>
        <option value="Home Builder">Home Builder</option>
        <option value="Home Energy Audit">Home Energy Audit</option>
        <option value="Home Inspection">Home Inspection</option>
        <option value="Home Remodeling">Home Remodeling</option>
        <option value="Home Security Systems">Home Security Systems</option>
        <option value="Home Staging">Home Staging</option>
        <option value="Home Theater Installation">Home Theater Installation</option>
        <option value="Home Warranty">Home Warranty</option>
        <option value="House Cleaning">House Cleaning</option>
        <option value="House Painting">House Painting</option>
        <option value="Hurricane Shutters">Hurricane Shutters</option>
        <option value="HVAC Companies">HVAC Companies</option>
        <option value="Insulation">Insulation</option>
        <option value="Interior Decorators">Interior Decorators</option>
        <option value="Interior Painting">Interior Painting</option>
        <option value="Iron Work">Iron Work</option>
        <option value="Irrigation System">Irrigation System</option>
        <option value="Jewelry Appraising">Jewelry Appraising</option>
        <option value="Land Surveyors">Land Surveyors</option>
        <option value="Landscape Lighting">Landscape Lighting</option>
        <option value="Large Appliances">Large Appliances</option>
        <option value="Lawn & Landscaping">Lawn & Landscaping</option>
        <option value="Lawn Care">Lawn Care</option>
        <option value="Lawn Mower Repair">Lawn Mower Repair</option>
        <option value="Lawn Treatment">Lawn Treatment</option>
        <option value="Lead Paint Removal">Lead Paint Removal</option>
        <option value="Leaf Removal">Leaf Removal</option>
        <option value="Leather Repair">Leather Repair</option>
        <option value="Lighting">Lighting</option>
        <option value="Locksmith">Locksmith</option>
        <option value="Mailbox Repair">Mailbox Repair</option>
        <option value="Marble & Granite">Marble & Granite</option>
        <option value="Masonry">Masonry</option>
        <option value="Metal Fabrication">Metal Fabrication</option>
        <option value="Mobile Home Remodeling">Mobile Home Remodeling</option>
        <option value="Mold Removal">Mold Removal</option>
        <option value="Movers">Movers</option>
        <option value="Mudjacking">Mudjacking</option>
        <option value="Mulch Delivering">Mulch Delivering</option>
        <option value="Nurseries">Nurseries</option>
        <option value="Oriental Rug Cleaning">Oriental Rug Cleaning</option>
        <option value="Outdoor Kitchens">Outdoor Kitchens</option>
        <option value="Patio Enclosures">Patio Enclosures</option>
        <option value="Patios">Patios</option>
        <option value="Pest Control">Pest Control</option>
        <option value="Phone Company">Phone Company</option>
        <option value="Phone Repair">Phone Repair</option>
        <option value="Piano Movers">Piano Movers</option>
        <option value="Plastering">Plastering</option>
        <option value="Playground Equipment Installation">Playground Equipment Installation</option>
        <option value="Plumbers">Plumbers</option>
        <option value="Pool Cleaning">Pool Cleaning</option>
        <option value="Pool Installers">Pool Installers</option>
        <option value="Pressure Washing">Pressure Washing</option>
        <option value="Professional Organizers">Professional Organizers</option>
        <option value="Radon Mitigation">Radon Mitigation</option>
        <option value="Real Estate Agent">Real Estate Agent</option>
        <option value="Real Estate Appraising">Real Estate Appraising</option>
        <option value="Roof Cleaning">Roof Cleaning</option>
        <option value="Roof Snow Removal">Roof Snow Removal</option>
        <option value="Roofing">Roofing</option>
        <option value="Rototilling">Rototilling</option>
        <option value="Satellite Tv">Satellite Tv</option>
        <option value="Screen Repair">Screen Repair</option>
        <option value="Septic Tank Service">Septic Tank Service</option>
        <option value="Sewer Cleaning">Sewer Cleaning</option>
        <option value="Siding Companies">Siding Companies</option>
        <option value="Skylight Installation">Skylight Installation</option>
        <option value="Small Appliance Repair">Small Appliance Repair</option>
        <option value="Snow Removal">Snow Removal</option>
        <option value="Solar Companies">Solar Companies</option>
        <option value="Stamped Concrete">Stamped Concrete</option>
        <option value="Stone & Gravel">Stone & Gravel</option>
        <option value="Structural Engineering">Structural Engineering</option>
        <option value="Stucco">Stucco</option>
        <option value="Tile Installation">Tile Installation</option>
        <option value="Trash Removal">Trash Removal</option>
        <option value="Tree Service">Tree Service</option>
        <option value="Upholstery">Upholstery</option>
        <option value="Upholstery Cleaning">Upholstery Cleaning</option>
        <option value="Wallpaper Hanger">Wallpaper Hanger</option>
        <option value="Wallpaper Removal">Wallpaper Removal</option>
        <option value="Water Damage Restoration">Water Damage Restoration</option>
        <option value="Water Heaters">Water Heaters</option>
        <option value="Water Softeners">Water Softeners</option>
        <option value="Welding">Welding</option>
        <option value="Well & Water Pump Repair">Well & Water Pump Repair</option>
        <option value="Window Cleaning">Window Cleaning</option>
        <option value="Window Replacement">Window Replacement</option>
        <option value="Window Security Film">Window Security Film</option>
        <option value="Window Tinting">Window Tinting</option>
        <option value="Window Treatment">Window Treatment</option>
        <option value="Woodworking">Woodworking</option>
      </select>

      <p><label for="state">State:</label></p>
      <select id="searchable-select" style="width: 100%;">
            <option value="Alabama">Alabama</option>
            <option value="Alaska">Alaska</option>
            <option value="Arizona">Arizona</option>
            <option value="Arkansas">Arkansas</option>
            <option value="California">California</option>
            <option value="Colorado">Colorado</option>
            <option value="Connecticut">Connecticut</option>
            <option value="Delaware">Delaware</option>
            <option value="District Of Columbia">District Of Columbia</option>
            <option value="Florida">Florida</option>
            <option value="Georgia">Georgia</option>
            <option value="Hawaii">Hawaii</option>
            <option value="Idaho">Idaho</option>
            <option value="Illinois">Illinois</option>
            <option value="Indiana">Indiana</option>
            <option value="Iowa">Iowa</option>
            <option value="Kansas">Kansas</option>
            <option value="Kentucky">Kentucky</option>
            <option value="Louisiana">Louisiana</option>
            <option value="Maine">Maine</option>
            <option value="Maryland">Maryland</option>
            <option value="Massachusetts">Massachusetts</option>
            <option value="Michigan">Michigan</option>
            <option value="Minnesota">Minnesota</option>
            <option value="Mississippi">Mississippi</option>
            <option value="Missouri">Missouri</option>
            <option value="Montana">Montana</option>
            <option value="Nebraska">Nebraska</option>
            <option value="Nevada">Nevada</option>
            <option value="New Hampshire">New Hampshire</option>
            <option value="New Jersey">New Jersey</option>
            <option value="New Mexico">New Mexico</option>
            <option value="New York">New York</option>
            <option value="North Carolina">North Carolina</option>
            <option value="North Dakota">North Dakota</option>
            <option value="Ohio">Ohio</option>
            <option value="Oklahoma">Oklahoma</option>
            <option value="Oregon">Oregon</option>
            <option value="Pennsylvania">Pennsylvania</option>
            <option value="Rhode Island">Rhode Island</option>
            <option value="South Carolina">South Carolina</option>
            <option value="South Dakota">South Dakota</option>
            <option value="Tennessee">Tennessee</option>
            <option value="Texas">Texas</option>
            <option value="Utah">Utah</option>
            <option value="Vermont">Vermont</option>
            <option value="Virginia">Virginia</option>
            <option value="Washington">Washington</option>
            <option value="West Virginia">West Virginia</option>
            <option value="Wisconsin">Wisconsin</option>
            <option value="Wyoming">Wyoming</option>
        </select>
        <p><label for="city">City:</label></p>
        <p><input type="text" name="city" id="city" placeholder="City"></p>

        <button type="submit" id="submitBtn">Start Scraping</button>
      </form>
      <!-- Loader element -->
      <div id="loader" style="display:none;"></div>
    </div>
    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <!-- Select2 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/css/select2.min.css" rel="stylesheet" />
    <!-- Select2 JS -->
    <script src="https://cdn.jsdelivr.net/npm/select2@4.1.0-rc.0/dist/js/select2.min.js"></script>
    <script>
    $(document).ready(function() {
      $('#searchable-select, #catg').select2({
        placeholder: "Select an option"
      });
      /****/
      $('#myForm').on('submit', function(event) {
        event.preventDefault(); // Prevent default form submission behavior

        // Show the loader
        $('#loader').show();
        $('#city, .select2, label, #submitBtn, #secondSelect').hide();

        // Simulate form submission delay (e.g., an AJAX request)
        setTimeout(function() {
          // Here you can add your form submission logic, like an AJAX request
          alert('Form submitted!');

          // Hide the loader after the submission process is complete
          $('#loader').hide();
        }, 2000); // Simulate a 2-second delay for demo purposes
      });
      /****/
    });
    /*****/
    $('#searchable-select').change(function() {
            const selectedCountry = $(this).val();  // Get the selected country value
            const $secondSelect = $('#secondSelect');  // Reference the second select

            // Hide all options in the second select
            $secondSelect.find('option').hide();

            if (selectedCountry) {
                // Show only the options that match the selected country value
                $secondSelect.find(`option[value="${selectedCountry}"]`).show();
            }

            // Reset the second select to the default option
            $secondSelect.val('');
        });
    </script>
</body>
</html>
'''

f.write(message)
f.close()
webbrowser.open_new_tab("1.html")