"""
Handle GeoHash
"""

import geohash


class Hasher():

    def encode_point(self, latitude, longitude):
        """
        Encodes the coordinates of a point into a GeoHash code

        Parameters:
            latitude (float): Latitude coordinate; ranges from -90° to +90°
            longitude (float): Longitude coordinate; ranges from -180° to +180°

        Returns:
            string: GeoHashed code
        """
        return geohash.encode(latitude, longitude) 

    def decode_point(code):
        """
        Decodes the GeoHash code into coordinates of a point

        Parameters:
            code (string): GeoHashed code

        Returns:
            float: Latitude coordinate; ranges from -90° to +90°
            float: Longitude coordinate; ranges from -180° to +180°
            
        """
        return geohash.decode(code) 



