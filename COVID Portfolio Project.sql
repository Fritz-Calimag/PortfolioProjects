SELECT *
FROM PortfolioProject..CovidDeaths
WHERE continent is not null
ORDER BY 3,4

--SELECT *
--FROM PortfolioProject..CovidVaccinations
--ORDER BY 3,4

SELECT location, date, total_cases, new_cases, total_deaths, population
FROM PortfolioProject..CovidDeaths
ORDER BY 1,2

--Looking at Total Cases vs Total Deaths
-- Shows likelihood of dying if you contract covid in your country during the year 2021
SELECT location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
FROM PortfolioProject..CovidDeaths
WHERE location like '%Phili%'
ORDER BY 1,2

-- Looking at total cases vs populations
--Shows what percentage of population got Covid
SELECT location, date, population, total_cases,  (total_cases/population)*100 as InfectionRate
FROM PortfolioProject..CovidDeaths
--WHERE location like '%Phili%'
ORDER BY 1,2

--Looking at countries with Highest Infection Rate compared to Population
SELECT location, population, MAX(total_cases) as HighestInfectionCount, MAX((total_cases/population))*100 as InfectionRate
FROM PortfolioProject..CovidDeaths
--WHERE location like '%Phili%'
GROUP BY location, population
ORDER BY InfectionRate DESC

--Showing the countries with Highest Death count compared to Population
--casted total death as integer for it was saved as nvarchar in the table
SELECT location, Max(cast(Total_deaths as int)) as TotalDeathCount
FROM PortfolioProject..CovidDeaths
WHERE continent is not null
--WHERE location like '%Phili%'
GROUP BY location
ORDER BY TotalDeathCount DESC

----Showing and grouping the continents with the highest death count
--SELECT location, Max(cast(Total_deaths as int)) as TotalDeathCount
--FROM PortfolioProject..CovidDeaths
--WHERE continent is null
----WHERE location like '%Phili%'
--GROUP BY location
--ORDER BY TotalDeathCount DESC

--Showing and grouping the continents with the highest death count
SELECT continent, Max(cast(Total_deaths as int)) as TotalDeathCount
FROM PortfolioProject..CovidDeaths
WHERE continent is not null
--WHERE location like '%Phili%'
GROUP BY continent
ORDER BY TotalDeathCount DESC


--GLOBAL NUMBERS

SELECT SUM(new_cases) as Total_cases, SUM(cast(new_deaths as int)) as Total_deaths, 
SUM(cast(new_deaths as int))/SUM(new_cases)*100 as DeathPercentage
FROM PortfolioProject..CovidDeaths
--WHERE location like '%Phili%'
WHERE continent is not null
--GROUP BY date
ORDER BY 1,2


-- Looking at Total Population vs Vaccinations

SELECT CVdeaths.continent, CVdeaths.location, CVdeaths.date, CVdeaths.population, CVvac.new_vaccinations
, SUM(CONVERT(int,CVvac.new_vaccinations)) OVER (Partition by cvdeaths.location ORDER BY cvdeaths.location
, cvdeaths.date) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
FROM PortfolioProject..CovidDeaths as CVdeaths
JOIN PortfolioProject..CovidVaccinations CVvac
	ON CVdeaths.location = CVvac.location 
	AND CVdeaths.date = CVvac.date
WHERE cvdeaths.continent is not null
ORDER BY 2,3

--Using a CTE we are showing the people rolling count of the total people vaccinated in comparison to their population
--from the start of the pandemic until April 30 2021

WITH Popvsvac (continent, location, date, population, new_vaccinations, RollingPeopleVaccinated)
as
(
SELECT CVdeaths.continent, CVdeaths.location, CVdeaths.date, CVdeaths.population, CVvac.new_vaccinations
, SUM(CONVERT(int,CVvac.new_vaccinations)) OVER (Partition by cvdeaths.location ORDER BY cvdeaths.location
, cvdeaths.date) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
FROM PortfolioProject..CovidDeaths as CVdeaths
JOIN PortfolioProject..CovidVaccinations CVvac
	ON CVdeaths.location = CVvac.location 
	AND CVdeaths.date = CVvac.date
WHERE cvdeaths.continent is not null
--ORDER BY 2,3
)
SELECT *, (RollingPeopleVaccinated/population)*100 as PercentPopVaccinated
FROM Popvsvac



--TEMP TABLE

DROP TABLE IF EXISTS #PercentPopulationVaccinated
CREATE TABLE #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)

INSERT INTO #PercentPopulationVaccinated
SELECT CVdeaths.continent, CVdeaths.location, CVdeaths.date, CVdeaths.population, CVvac.new_vaccinations
, SUM(CONVERT(int,CVvac.new_vaccinations)) OVER (Partition by cvdeaths.location ORDER BY cvdeaths.location
, cvdeaths.date) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
FROM PortfolioProject..CovidDeaths as CVdeaths
JOIN PortfolioProject..CovidVaccinations CVvac
	ON CVdeaths.location = CVvac.location 
	AND CVdeaths.date = CVvac.date
--WHERE cvdeaths.continent is not null
--ORDER BY 2,3

SELECT *, (RollingPeopleVaccinated/population)*100 as PercentPopVaccinated
FROM #PercentPopulationVaccinated


-- Creating View to store data for later

CREATE VIEW PercentPopulationVaccinated as
SELECT CVdeaths.continent, CVdeaths.location, CVdeaths.date, CVdeaths.population, CVvac.new_vaccinations
, SUM(CONVERT(int,CVvac.new_vaccinations)) OVER (Partition by cvdeaths.location ORDER BY cvdeaths.location
, cvdeaths.date) as RollingPeopleVaccinated
--, (RollingPeopleVaccinated/population)*100
FROM PortfolioProject..CovidDeaths as CVdeaths
JOIN PortfolioProject..CovidVaccinations CVvac
	ON CVdeaths.location = CVvac.location 
	AND CVdeaths.date = CVvac.date
WHERE cvdeaths.continent is not null
--ORDER BY 2,3

SELECT *
FROM PercentPopulationVaccinated