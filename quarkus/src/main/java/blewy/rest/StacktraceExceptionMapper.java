package blewy.rest;

import jakarta.annotation.Priority;
import jakarta.enterprise.context.ApplicationScoped;
import jakarta.ws.rs.Priorities;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import jakarta.ws.rs.ext.ExceptionMapper;
import jakarta.ws.rs.ext.Provider;

import org.jboss.logging.Logger;

import java.util.Arrays;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * Global catch-all mapper that exposes the real exception message and stack trace
 * in every response (HTTP 500).  Very useful for debugging; **do not** enable in
 * production unless you are comfortable leaking internals.
 */
@Provider
@ApplicationScoped
@Priority(Priorities.USER)          // outranks Quarkus’ default mappers
public class StacktraceExceptionMapper implements ExceptionMapper<Throwable> {

    private static final Logger LOG = Logger.getLogger(StacktraceExceptionMapper.class);

    @Override
    public Response toResponse(Throwable exception) {
        // 1. log full details
        LOG.error("Unhandled exception caught by StacktraceExceptionMapper", exception);

        // 2. build readable stack trace string
        String stack = Arrays.stream(exception.getStackTrace())
                             .map(StackTraceElement::toString)
                             .collect(Collectors.joining("\n"));

        // 3. put everything in a simple JSON structure
        Map<String, Object> body = Map.of(
                "exception",   exception.getClass().getName(),
                "message",     exception.getMessage(),
                "stackTrace",  stack
        );

        // 4. return 500 with full payload
        return Response.serverError()
                       .type(MediaType.APPLICATION_JSON)
                       .entity(body)
                       .build();
    }
}
