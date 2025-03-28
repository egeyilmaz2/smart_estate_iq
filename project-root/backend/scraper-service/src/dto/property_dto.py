from dataclasses import dataclass, field
from typing import List, Optional, Tuple
import datetime

@dataclass
class PropertyDTO:
    property_id: Optional[int] = None        # Unique identifier for the property
    title: str = ""                            # Title or headline of the property listing
    description: str = ""                      # Detailed description of the property
    property_type: str = ""                    # Type of property (e.g., apartment, house, villa, etc.)
    price: float = 0.0                         # Price of the property
    currency: str = "TRY"                      # Currency (defaulting to Turkish Lira, adjust as needed)
    area: float = 0.0                          # Total area in square meters (or as specified)
    area_unit: str = "sqm"                     # Unit of area measurement (e.g., sqm, sqft)
    address: str = ""                          # Full address of the property
    city: str = ""                             # City where the property is located
    district: str = ""                         # District or region within the city
    neighborhood: str = ""                     # Neighborhood name
    floor: Optional[int] = None                # The floor on which the property is located (if applicable)
    total_floors: Optional[int] = None         # Total number of floors in the building (if applicable)
    number_of_bedrooms: int = 0                # Number of bedrooms
    number_of_bathrooms: int = 0               # Number of bathrooms
    has_balcony: bool = False                  # Whether the property has a balcony
    has_parking: bool = False                  # Whether the property includes parking space
    has_garden: bool = False                   # Whether the property has a garden
    has_pool: bool = False                     # Whether there is a swimming pool
    year_built: Optional[int] = None           # Year the property was built
    is_new_build: bool = False                 # Indicates if the property is a new construction
    status: str = ""                           # Listing status (e.g., "for sale", "for rent")
    listing_date: Optional[datetime.date] = None  # Date the property was listed
    image_urls: List[str] = field(default_factory=list)  # URLs of property images
    features: List[str] = field(default_factory=list)    # Additional features (e.g., "Central Heating", "Air Conditioning")
    geo_coordinates: Optional[Tuple[float, float]] = None  # (latitude, longitude)
    heating_type: str = ""                     # Type of heating (e.g., "Central", "Natural Gas", "Electric")
