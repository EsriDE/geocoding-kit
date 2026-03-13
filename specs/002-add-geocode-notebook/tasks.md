# Tasks: Add Geocode Notebook

**Input**: Design documents from `/specs/002-add-geocode-notebook/`  
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the example notebook scaffold and ensure required assets exist.

- [ ] T001 Create `examples/geocode_notebook.ipynb` with basic cells for imports, data loading, and placeholder geocoding logic
- [ ] T002 Verify `examples/addresses.csv` exists and contains sample address rows (create a minimal sample row if missing)
- [ ] T003 [P] Ensure `pyproject.toml` and `requirements.txt` includes `arcgis` and `arcgis-mapping` (or document required dependencies)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Provide the reusable pieces the notebook will reference.

- [ ] T004 [P] Add a short helper cell in `examples/geocode_notebook.ipynb` to load addresses into a pandas DataFrame from `examples/addresses.csv`
- [ ] T005 [P] Add clear markdown instructions in `examples/geocode_notebook.ipynb` describing where to configure ArcGIS credentials and how to install dependencies

---

## Phase 3: User Story 1 - View Geocoded Results in Notebook (Priority: P1) 🎯 MVP

**Goal**: Deliver a runnable notebook that reads addresses and displays geocoded results.

**Independent Test**: Open `examples/geocode_notebook.ipynb`, run all cells, and confirm a DataFrame of geocoded results is displayed.

- [ ] T006 [US1] Add a code cell in `examples/geocode_notebook.ipynb` that calls the geocoding-kit geocode function and stores results in a DataFrame
- [ ] T007 [US1] Add a code cell in `examples/geocode_notebook.ipynb` that displays the geocode results (matched address, latitude, longitude, confidence)

---

## Phase 4: User Story 2 - Learn ArcGIS Module Usage (Priority: P2)

**Goal**: Show how to use `arcgis` and `arcgis-mapping` within the notebook for geocoding operations.

**Independent Test**: Review `examples/geocode_notebook.ipynb` and confirm it imports `arcgis` and `arcgis.mapping` and includes explanatory text.

- [ ] T008 [US2] Add a code cell in `examples/geocode_notebook.ipynb` importing `arcgis` and `arcgis.mapping` and initializing a `GIS` object
- [ ] T009 [US2] Add a markdown cell in `examples/geocode_notebook.ipynb` explaining how the `arcgis` and `arcgis-mapping` modules are used in the notebook

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Ensure the notebook is clear, documented, and discoverable.

- [ ] T010 [P] Update `specs/002-add-geocode-notebook/quickstart.md` to reference `examples/geocode_notebook.ipynb`
- [ ] T011 [P] Confirm `examples/geocode_notebook.ipynb` includes clear step-by-step instructions and is runnable end-to-end

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion (notebook and sample data available)
- **User Stories (Phase 3+)**: Depend on Foundational phase completion
- **Polish (Final Phase)**: Depends on user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational phase is ready
- **User Story 2 (P2)**: Can start after Foundational phase is ready; works independently of US1

### Parallel Opportunities

- Tasks marked **[P]** (T003, T004, T005, T010, T011) can be executed in parallel
- User story tasks (T006..T009) can be implemented in parallel once foundational tasks are complete

---

## Parallel Example: User Story 1

```bash
# While foundational tasks are in progress, another contributor can work on the notebook logic:
# 1) Create the geocode results cell (T006)
# 2) Add results display cell (T007)
```
