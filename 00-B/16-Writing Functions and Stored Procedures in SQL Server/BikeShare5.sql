CREATE DATABASE BikeShare;
GO

USE BikeShare;
GO

CREATE TABLE CapitalBikeShare (ID INT, Duration INT, StartDate DATETIME2(7), EndDate DATETIME2(7), StartStationNumber INT, StartStation VARCHAR(100), EndStationNumber INT, EndStation VARCHAR(100), BikeNumber VARCHAR(50), MemberType VARCHAR(50));
GO

BULK INSERT CapitalBikeShare FROM '/home/repl/BikeShare-pipe.csv' WITH(FIELDTERMINATOR =',', ROWTERMINATOR = '\n');
GO

CREATE TABLE [dbo].[RideSummary]([Date] [date] NOT NULL, [RideHours] [numeric](18, 0) NOT NULL);
GO

INSERT INTO [dbo].[RideSummary] (Date, RideHours)
VALUES ('3/1/2018', 388)
GO
