# Pair 4 responses and state

Confirm these APIs in the installed release. In an application, inspect `vendor/viames/pair/src`; in the framework checkout, inspect `src`. `Web/Controller.php`, `Web/PageResponse.php`, `Http/Input.php`, and `Data/ReadModel.php` own these contracts.

An illustrative read-only page, after application bootstrap and class loading:

```php
use Pair\Web\Controller;
use Pair\Web\PageResponse;

final readonly class ExamplePageState {

	/** Build the layout's explicit state. */
	public function __construct(public string $title) {}

}

final class ExampleController extends Controller {

	/** Render the page from prepared state. */
	public function defaultAction(): PageResponse {
		return $this->page('default', new ExamplePageState('Example'), 'Example');
	}

}
```

Place the classes in separate files and follow the application's loading rules. The layout reads `$state->title` and escapes it for its output context. A plain typed object is sufficient for `page()`; it need not implement `ReadModel` unless the contract needs serialization.

`Pair\Data\ReadModel` extends `JsonSerializable` and requires `toArray()`. A class implementing it must satisfy both contracts; `ArraySerializableData` supplies the JSON export behavior used by the generator. `MapsFromRecord::fromRecord(ActiveRecord $record): static` supports explicit ORM mapping. Prefer an application-specific typed contract over dumping a record or adding a `Payload` fallback.

Use the web controller's immutable `input()` accessors for request extraction, followed by domain validation and authorization. Typed extraction alone does not establish validity or ownership.

Choose the existing response contract deliberately: `page()` renders HTML, `json()` returns a JSON response, and `dataResponse()` / `problemResponse()` provide the web AJAX envelopes when present in the installed version. Changing an existing envelope requires reviewing its consumers. API controllers have their own helpers and middleware; see `pair:api-safety`.
